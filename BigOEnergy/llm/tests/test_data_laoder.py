import pytest
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
from src.data_loader import ACDataset

@pytest.fixture(scope="module")
def tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    return tokenizer

def tests_dataset_loads(tmp_path, tokenizer):
    file_path = tmp_path / "train.txt"
    file_path.write_text("Human: Hello\nAI: Hi!\n\nHuman: Bye\nAI: Cya")
    dataset = ACDataset(str(file_path), tokenizer)
    assert len(dataset) == 2

def test_data_item_structure(tmp_path, tokenizer):
    file_path = tmp_path/ "train.txt"
    file_path.write_text("Human: Hello\nAI: Hi!")
    dataset = ACDataset(str(file_path), tokenizer)
    item = dataset[0]
    assert set(item.keys()) == {"input_ids", "attention_mask", "labels"}
    assert item["input_ids"].shape == item["attention_mask"].shape
    assert item["labels"].shape == item["input_ids"].shape

def test_dataloader_batches(tmp_path):
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

    (tmp_path / "train_conversations.txt").write_text("Human: Hi\nAI: Hello\n\nHuman: Bye\nAI: Goodbye")
    (tmp_path / "val_conversations.txt").write_text("Human: Test\nAI: Response")

    train_loader, val_loader, _ = ACDataset.create_data_loaders(
        data_dir=str(tmp_path), model_name="gpt2", batch_size=2
    )

     # Train loader checks
    train_batch = next(iter(train_loader))
    assert "input_ids" in train_batch
    assert train_batch["input_ids"].shape[0] == 2

    # Val loader checks
    val_batch = next(iter(val_loader))
    assert "input_ids" in val_batch
    assert val_batch["input_ids"].shape[0] == 1  # only one sample