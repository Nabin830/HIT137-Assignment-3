from PIL import Image
from ...models.image_classifier import ImageClassifier
from .base import BaseTask


class ImageTask(BaseTask):
    """Runs image classification using ImageClassifier (ViT Base)."""

    def __init__(self):
        super().__init__()
        self._model = ImageClassifier()

    # Method overriding
    def run(self, data) -> dict:
        img = Image.open(data) if isinstance(data, str) else data
        out = self._model.infer(img)
        self._set_last_result(out)
        return out

    def info(self) -> str:
        return "Image classification (ViT Base). Input: image path or PIL.Image. Output: label + score."
