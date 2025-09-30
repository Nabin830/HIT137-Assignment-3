from transformers import pipeline  # Importing the  Hugging Face pipeline
from PIL import Image  # it is used for  opening images
from .base import HFModelBase, LoggingMixin, CachingMixin
from ..utils.decorators import timed, validate_input


class ImageClassifier(LoggingMixin, CachingMixin, HFModelBase):

    def __init__(self, model_id: str = "apple/mobilevit-x-small"):
        super().__init__(model_id)  # Call base class constructor
        # Creating  the Hugging Face pipeline for image classifications
        self._set_pipeline(pipeline("image-classification", model=model_id))

    @timed  # Added elapsed time
    @validate_input((str, Image.Image))
    def infer(self, data):
        path = (
            data if isinstance(data, str) else getattr(data, "filename", "<PIL Image>")
        )
        self.log("image_infer_start", {"path": path})  # Log the attempt
        key = ("img", path)  # Created the  cache key using image path

        cached = self.get_cache(key)
        if cached:  # If already cached then return it
            return cached

        img = (
            Image.open(data) if isinstance(data, str) else data
        )  # Open the image when the path is given
        results = self._pipe()(img)  # Get all results from pipeline

        # Return top 5 results with detailed information
        top_results = []
        for i, res in enumerate(results[:5]):
            top_results.append({"label": res["label"], "score": float(res["score"])})

        # Primary result for backward compatibility
        primary = results[0]
        out = {
            "label": primary["label"],
            "score": float(primary["score"]),
            "top_predictions": top_results,
            "description": self._generate_description(top_results),
        }
        self.set_cache(key, out)  # Cache result
        return out

    def _generate_description(self, results):
        """Generate a human-readable description from classification results"""
        if not results:
            return "No classification results available."

        # Get top result
        top = results[0]
        description = f"This image appears to be of {top['label']} (confidence: {top['score']:.1%})"

        # Add additional details if there are other significant predictions
        significant_others = [
            r for r in results[1:3] if r["score"] > 0.1
        ]  # >10% confidence
        if significant_others:
            other_labels = [
                f"{r['label']} ({r['score']:.1%})" for r in significant_others
            ]
            description += f". It may also contain: {', '.join(other_labels)}"

        description += "."
        return description

    def info(self) -> str:
        # Description of this model for GUI/info display
        return "Image classification (MobileViT X-Small). Input: image path or PIL Image. Output: top predictions with detailed descriptions of image contents."
