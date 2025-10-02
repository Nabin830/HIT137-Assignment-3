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
