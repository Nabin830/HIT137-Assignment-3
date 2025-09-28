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

### Enhanced User Experience

🎯 **Smart Interface Design**

- **Dynamic Input Display**: Only relevant inputs shown based on model selection
- **Real-time Status Updates**: Color-coded status indicators and progress animations
- **Asynchronous Processing**: Non-blocking UI with background AI inference
- **Intelligent Navigation**: Auto-switch to Output tab with user confirmation

🚀 **Professional Styling**

- **Modern Theme**: Clean, professional appearance with custom styling
- **Visual Tabs**: Icon-enhanced tab names (🚀📊ℹ️🏗️)
- **Enhanced Typography**: Improved fonts and consistent spacing
- **Status Bar**: Current status and version information

### Tabs

1. **🚀 Run Analysis**: Smart model selection with context-aware inputs
2. **📊 Output**: Timestamped, formatted results with counter
3. **ℹ️ Model Info**: Detailed AI model specifications
4. **🏗️ OOP Concepts**: Comprehensive OOP explanations

### Enhanced Widgets

- **Smart Dropdowns**: Model selection with automatic input switching
- **Rich Text Areas**: Formatted input/output with syntax highlighting
- **Interactive Buttons**: Status-aware buttons with visual feedback
- **Progress Indicators**: Real-time processing animations
- **File Browser**: Enhanced image selection with preview info
- **Menu System**: Quick navigation and utility functions

### User Experience Improvements

✨ **Status & Feedback**

- Real-time processing status with color coding
- Progress animations during model inference
- Success/error notifications with helpful messages
- Result counter and timestamps in output

🎯 **Smart Input Management**

- Pre-filled example data for quick testing
- Input validation with helpful error messages
- Context-aware input visibility (text vs image)
- Smart clearing with restoration of defaults

🚀 **Navigation & Flow**

- Quick tab switching via buttons and menus
- Automatic output tab switching option
- Keyboard shortcuts and menu navigation
- Professional about dialog with project info

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
