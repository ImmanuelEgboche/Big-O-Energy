import torch
import os
import sys
from datetime import datetime
from pathlib import Path
import json
from tqdm import tqdm
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_loader import create_data_loaders
from src.model import setup_model_and_tokenizer, save_model, print_model_info
from config import Config

class AnimeTrainer:
    def __init__(self, config=None):
        self.config = config or Config()
        self.model = None
        self.tokenizer = None
        self.device = None
        self.optimizer = None
        self.train_loader = None
        self.val_loader = None
        self.train_losses = []
        self.val_losses = []
        self.best_val_loss = float('inf')

    def setup_directories(self):
        directories = [
            self.config.OUTPUT_DIR + "/logs",
            self.config.OUTPUT_DIR + "/samples",
            self.config.MODEL_DIR + '/checkpoints',
            self.config.MODEL_DIR + "/final"
        ]

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)

    
    def setup(self):
        print("Setting up training environement...")

        self.model, self.tokenizer, self.device = setup_model_and_tokenizer(
            model_name=self.config.MODEL_NAME
        )

        print_model_info(self.model, self.tokenizer)

        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config.LEARNING_RATE,
            weight_decay=0.01
        )

        self.train_loader, self.val_loader, _ = create_data_loaders(
            data_dir=self.config.DATA_DIR,
            model_name=self.config.MODEL_NAME,
            batch_size=self.config.BATCH_SIZE,
            max_length=self.config.MAX_LENGTH
        )

        print(f"setup done 👍")

    def train_epoch(self, epoch):
        self.model.train()
        total_loss = 0
        num_batches = len(self.train_loader)

        #Porgress bar
        pbar = tqdm(self.train_loader, desc=f"Epoch {epoch+1}/{self.config.NUM_EPOCHS}")

        for batch_idx, batch in enumerate(pbar):
            input_ids = batch['input_ids'].to(self.device)
            attention_mask = batch['attention_mask'].to(self.device)
            labels = batch['labels'].to(self.device)
        
            self.optimizer.zero_grad()

            outputs = self.model(
                input_ids = input_ids,
                attention_mask = attention_mask,
                labels = labels
            )

            loss = outputs.loss

            loss.backward()

            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)

            self.optimizer.step()

            total_loss += loss.item()
            avg_loss = total_loss / (batch_idx + 1)

            pbar.set_postfix({
                'loss': f'{loss.item():.4f}',
                'avg_loss': f'{avg_loss:.4f}'
            })

            if batch_idx % 50 == 0:
                self.log_training_step(epoch, batch_idx, loss.item(), avg_loss)
       
        epoch_loss = total_loss / num_batches
        self.train_losses.append(epoch_loss)

        return epoch_loss

    def validate(self, epoch):
        self.model.eval()
        total_loss = 0
        num_batches = len(self.val_loader)

        with torch.no_grad():
            for batch in tqdm(self.val_loader, desc="Validating"):
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    labels=labels
                )

                loss = outputs.loss
                total_loss += loss.item()
        

        val_loss = total_loss / num_batches
        self.val_losses.append(val_loss)

        print(f"validation loss {val_loss:.4f}")

        if val_loss < self.best_val_loss:
            self.best_val_loss = val_loss
            self.save_checkpoint(epoch, is_best=True)
            print("New best model saved")
        
        return val_loss
    
    def generate_sample(self, prompt="Human: I want something like Naruto\nAI:"):
        """Generate a sample to see training progress"""
        self.model.eval()
        
        with torch.no_grad():
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.config.MAX_NEW_TOKENS,
                do_sample=True,
                temperature=self.config.TEMPERATURE,
                top_k=self.config.TOP_K,
                top_p=self.config.TOP_P,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response

    def train(self):
        print("Starting training ⌛")
        start_time = datetime.now()

        for epoch in range(self.config.NUM_EPOCHS):
            print(f"\n Epoch {epoch + 1}/ {self.config.NUM_EPOCHS}")

            train_loss = self.train_epoch(epoch)

            val_loss = self.validate(epoch)

            sample = self.generate_sample()
            print(f"sameple generation: \n{sample}")

            self.save_sample(epoch, sample, train_loss, val_loss)

            self.save_checkpoint(epoch)

            print(f"EPOCH {epoch + 1} Summary:")
            print(f" Train Loss: {train_loss:.4f}")
            print(f"Val loss: {val_loss:.4f}")
        
        end_time = datetime.now()
        training_time = end_time - start_time

        print(f"\n Training done 👍")
        print(f"⏱️  Total time: {training_time}")
        print(f"📉 Best validation loss: {self.best_val_loss:.4f}")

        self.save_final_model()

        self.plot_training_curves()
    
    def save_checkpoint(self, epoch, is_best=False):
        """Save training checkpoint"""
        checkpoint_dir = f"{self.config.MODEL_DIR}/checkpoints"

        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'train_losses': self.train_losses,
            'val_losses': self.val_losses,
            'best_val_loss': self.best_val_loss,
            'config': vars(self.config)
        }

        torch.save(checkpoint, f"{checkpoint_dir}/latest.pt")

        if is_best:
            torch.save(checkpoint, f"{checkpoint_dir}/best.pt")

    def save_final_model(self):
        final_path = f"{self.config.MODEL_DIR}/final/anime-recommender"
        save_model(self.model, self.tokenizer, final_path, self.config)

        history = {
            'train_losses': self.train_losses,
            'val_losses': self.val_losses,
            'best_val_loss': self.best_val_loss,
            'config': vars(self.config)
        }

        with open(f"{final_path}/training_history.json", 'w') as f:
            json.dump(history, f, indent=2)

    def save_sample(self, epoch, sample, train_loss, val_loss):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sample_file = f"{self.config.OUTPUT_DIR}/samples/epoch_{epoch+1}_{timestamp}.txt"

        with open(sample_file, 'w') as f:
            f.write(f"Epoch: {epoch + 1}\n")
            f.write(f"Train Loss: {train_loss:.4f}\n")
            f.write(f"Val Loss: {val_loss:.4f}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"\n--- Generated Sample ---\n")
            f.write(sample)
    
    def log_training_step(self, epoch, batch_idx, loss, avg_loss):
        log_file = f"{self.config.OUTPUT_DIR}/logs/training.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Epoch {epoch + 1}, Batch {batch_idx}, Loss: {loss:.4f}, Avg Loss: {avg_loss:.4f}\n")
    
    def plot_training_curves(self):
        plt.figure(figsize=(12,5))

         # Plot losses
        plt.subplot(1, 2, 1)
        epochs = range(1, len(self.train_losses) + 1)
        plt.plot(epochs, self.train_losses, 'b-', label='Training Loss')
        plt.plot(epochs, self.val_losses, 'r-', label='Validation Loss')
        plt.title('Training and Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.grid(True)
        
        # Plot learning curve
        plt.subplot(1, 2, 2)
        plt.plot(epochs, self.val_losses, 'g-', label='Validation Loss')
        plt.title('Learning Curve')
        plt.xlabel('Epoch')
        plt.ylabel('Validation Loss')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig(f"{self.config.OUTPUT_DIR}/training_curves.png")
        plt.show()
        
        print(f"📊 Training curves saved to {self.config.OUTPUT_DIR}/training_curves.png")

def main():
    """Main"""

    config = Config()

    print("AND SO IT BEGINS")
    print("=" * 50)

    trainer = AnimeTrainer(config)
    trainer.setup_directories() 
    trainer.setup()

    trainer.train()

    print("\n🎉 Training complete!")
    print(f"Outputs in: {config.OUTPUT_DIR}")
    print(f"Final model saved in: {config.MODEL_DIR}/final/anime-recommender")


if __name__ == "__main__":
    main()


