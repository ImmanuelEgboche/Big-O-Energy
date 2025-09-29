from pathlib import Path

class Config:
    # Model settings
    MODEL_NAME = "gpt2"
    MAX_LENGTH = 512
    
    # Training settings
    BATCH_SIZE = 4
    LEARNING_RATE = 5e-5
    NUM_EPOCHS = 3
    WARMUP_STEPS = 100
    
    BASE_DIR = Path(__file__).parent  # Get project root
    DATA_DIR = str(BASE_DIR / "data/processed")
    MODEL_DIR = str(BASE_DIR / "models")
    OUTPUT_DIR = str(BASE_DIR / "outputs")
    
    # Generation settings
    MAX_NEW_TOKENS = 150
    TEMPERATURE = 0.8
    TOP_K = 50
    TOP_P = 0.95