import torch
from torch.utils.data import Dataset, Dataloader
from transformers import AutoTokenizer
import os

class ACDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=512):
        self.conversations = []
        self.tokenizer = tokenizer
        self.max_length = max_length

        # Load conversations from file
        print("Loading convos from {fie_path}.")
        with open(file_path, 'r', encoding='utf-8') as f:
            content =f.read().strip()
            # Split on double new lines as each convo is seperated by \n\n
            self.conversations = [convo.strip() for convo in content.split('\n\n') if convo.strip()]
        print( f"⚠️loaded {len(self.conversations)} convos⚠️")
    
    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, idx):
        """
        Gets a single conversation and converts it to tokens

        Returns a dict with input_ids attention_mask and labels
        """

        conversation = self.conversations[idx]

        # Tokenise the convo
        encoded = self.tokenizer(
            conversation,
            truncation=True,
            padding = 'max_length',
            return_tensors='pt'
        )

        input_ids = encoded['input_ids'].squeeze()
        attention_mask = encoded['attention_mask'].squeeze()

        #For causal language modeling, labels are the same as input_ids
        # The model learns to predict the next token
        labels = input_ids.clone()

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': labels 
        }
    def create_data_loaders(data_dir="data/processed", model_name="gpt2", batch_size=4, max_length=512):
        """
        """
        print(f"Setting up tokenizer for {model_name}")

        #Load tokeniser
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Add padding token
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            print("Adding padding token")
        
        # Create datasets
        train_dataset = ACDataset(
        file_path=f"{data_dir}/train_conversations.txt",
        tokenizer=tokenizer,
        max_length=max_length
        )
    
        val_dataset = ACDataset(
            file_path=f"{data_dir}/val_conversations.txt",
            tokenizer=tokenizer,
            max_length=max_length
        )

        # Create data laoders
        train_loader = Dataloader(
            train_dataset,
            batch_size = batch_size,
            shuffle= True,
            num_workers = 0
        )

        val_loader = Dataloader(
            val_dataset,
            batch_size = batch_size,
            shuffle=False,
            num_workers = 0
        )

        print(f"Data loaders created:")
        print(f" Train batches: {len(train_loader)}")
        print(f" Val batches: {len(val_loader)}")
        print(f" batch size: {batch_size}")

        return train_loader, val_loader, tokenizer