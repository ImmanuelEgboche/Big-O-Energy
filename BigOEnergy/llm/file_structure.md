llm/
├── README.md                           # Portfolio documentation
├── requirements.txt                    # Dependencies
├── config.py                          # Model settings
│
├── data/
│   ├── processed/
│   │   ├── train_conversations.txt     # Ready for training
│   │   ├── val_conversations.txt       # Validation set
│   │   └── test_conversations.txt      # Test set
│   └── create_dataset.py              # Data processing script
│
├── src/
│   ├── data_loader.py                 # Load and format data
│   ├── model.py                       # Model setup
│   ├── trainer.py                     # Training logic
│   └── generator.py                   # Text generation
│
├── scripts/
│   ├── scrape_data.py                 # Collect anime data
│   ├── train_model.py                 # Main training script
│   ├── evaluate.py                    # Test the model
│   └── demo.py                        # Interactive demo
│
├── models/
│   ├── base/                          # Original GPT-2
│   ├── checkpoints/                   # Training saves
│   └── final/                         # Your trained model
│
├── notebooks/
│   ├── data_exploration.ipynb         # Show your data work
│   ├── training_analysis.ipynb        # Training metrics
│   └── demo.ipynb                     # Interactive showcase
│
└── outputs/
    ├── logs/                          # Training logs
    ├── samples/                       # Generated examples
    └── evaluation/                    # Test results