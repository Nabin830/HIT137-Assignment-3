from abc import ABC, abstractmethod

# Lazy import - only import models when needed
# from app.models.sentiment_model import SentimentModel
# from app.models.image_model import ImageClassifier


class BaseTask(ABC):
    """Abstract base class for all tasks - demonstrates polymorphism"""

    @abstractmethod
    def run(self, data) -> dict:
        """All tasks must implement this method"""
        pass


class SentimentTask(BaseTask):
    """Task wrapper for sentiment analysis model"""

    def __init__(self):
        self.model = None  # Lazy loading

    def run(self, data: str) -> dict:
        """Run sentiment analysis on text data"""
        if self.model is None:
            print("Loading sentiment model...")
            from app.models.sentiment_model import SentimentModel

            self.model = SentimentModel()
        return self.model.infer(data)


class ImageTask(BaseTask):
    """Task wrapper for image classification model"""

    def __init__(self):
        self.model = None  # Lazy loading

    def run(self, data: str) -> dict:
        """Run image classification on image file path"""
        if self.model is None:
            print("Loading image classification model...")
            from app.models.image_model import ImageClassifier

            self.model = ImageClassifier()
        return self.model.infer(data)
