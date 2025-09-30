from ...models.sentiment_model import SentimentModel
from .base import BaseTask


class SentimentTask(BaseTask):
    """Runs text sentiment inference using SentimentModel."""

    def __init__(self):
        super().__init__()
        # Encapsulation: keep model private-ish
        self._model = SentimentModel()

    # Method overriding
    def run(self, data: str) -> dict:
        out = self._model.infer(data)
        self._set_last_result(out)
        return out

    def info(self) -> str:
        return "Sentiment analysis (Transformers). Input: text. Output: label + score."
