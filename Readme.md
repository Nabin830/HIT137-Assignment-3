# HIT137 Assignment 3 - AI Model Demo GUI

A comprehensive Tkinter-based GUI application demonstrating Object-Oriented Programming concepts with integrated Hugging Face AI models.

## 🎯 Project Overview

This project implements a dual-purpose AI system with:

- **Sentiment Analysis**: Text sentiment classification using DistilBERT
- **Image Classification**: Image categorization using MobileViT

## 🏗️ OOP Concepts Demonstrated

### 1. Multiple Inheritance

- `SentimentModel` and `ImageClassifier` inherit from multiple classes:
  - `HFModelBase` (abstract base class)
  - `LoggingMixin` (logging functionality)
  - `CachingMixin` (caching functionality)

### 2. Multiple Decorators

- `@timed`: Measures execution time of model inference
- `@validate_input`: Validates input data types

### 3. Encapsulation

- Private attributes: `__pipe` (hidden pipeline)
- Protected methods: `_set_pipeline()`, `_pipe()`
- Public interface: `infer()`, `info()`

### 4. Polymorphism

- `BaseTask` defines common interface
- `SentimentTask` and `ImageTask` implement `run()` method differently
- Controller uses tasks uniformly: `task.run(data)`

### 5. Method Overriding

- Each task class overrides `BaseTask.run()` with specific implementation

## 🚀 How to Run

### Prerequisites

```bash
pip install -r requirements.txt
```

### GUI Application

```bash
python -m app.main
```

### Command Line Interface

```bash
# Sentiment Analysis
python cli.py sentiment --text "I love this project!"

# Image Classification
python cli.py image --path "assets/sample.jpg"
```

### Test Models

```bash
python -m app.test_models
```

## 📱 GUI Features

### Tabs

1. **Run**: Select models, input data, execute AI models
2. **Output**: View inference results
3. **Model Info**: AI model descriptions and capabilities
4. **OOP Concepts**: Explanations of OOP concepts used

### Widgets

- **Dropdown menus**: Model selection, input type
- **Text areas**: Input text, output display
- **Buttons**: Run, Clear, Browse, Exit
- **File dialog**: Image file selection
- **Menu bar**: File operations

## 🤖 AI Models Used

### Sentiment Analysis

- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Category**: Natural Language Processing (NLP)
- **Input**: Text string
- **Output**: Sentiment label (POSITIVE/NEGATIVE) + confidence score

### Image Classification

- **Model**: `apple/mobilevit-x-small`
- **Category**: Computer Vision
- **Input**: Image file path or PIL Image
- **Output**: Classification label + confidence score

## 📁 Project Structure

```
HIT137-Assignment-3/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main GUI entry point
│   ├── test_models.py       # Model testing functions
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main.py          # GUI main window
│   │   ├── controllers.py   # Application logic
│   │   ├── views.py         # GUI components
│   │   └── tasks.py         # Model task wrappers
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py          # Base classes and mixins
│   │   ├── sentiment_model.py # Sentiment analysis model
│   │   └── image_model.py   # Image classification model
│   └── utils/
│       ├── __init__.py
│       └── decorators.py    # Custom decorators
├── assets/
│   └── sample.jpg           # Sample image for testing
├── cli.py                   # Command-line interface
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🔧 Technical Details

### Performance Optimizations

- **Lazy Loading**: Models load only when first used
- **Caching**: Results cached to avoid repeated computations
- **Timed Execution**: Performance monitoring with decorators

### Error Handling

- Input validation decorators
- Comprehensive exception handling
- User-friendly error messages

### Code Quality

- Proper package structure with `__init__.py` files
- Type hints and documentation
- Clean separation of concerns
- Professional code organization

## 📋 Assignment Requirements Fulfilled

✅ **Tkinter GUI with OOP concepts**  
✅ **Multiple inheritance, decorators, encapsulation**  
✅ **Polymorphism and method overriding**  
✅ **Two HF models from different categories**  
✅ **User input selection and model execution**  
✅ **OOP explanations section in GUI**  
✅ **Model information section**  
✅ **Complete set of GUI widgets**  
✅ **Proper code organization across multiple files**  
✅ **Free, reasonably-sized HF models**  
✅ **Direct model integration via libraries**

## 👥 Authors

- **Ashish Bhusal** - Implementation and Development
- **HIT137** - Software Now Assignment 3

## 📄 License

This project is submitted as part of HIT137 Software Now course requirements.
