from transformers import pipeline                     # Importing the  Hugging Face pipeline
from PIL import Image                                 # it is used for  opening images
from .base import HFModelBase, LoggingMixin, CachingMixin
from app.utils.decorators import timed, validate_input

class ImageClassifier(LoggingMixin, CachingMixin, HFModelBase):

    def __init__(self, model_id: str = "apple/mobilevit-x-small"):
        super().__init__(model_id)                    # Call base class constructor
        # Creating  the Hugging Face pipeline for image classifications
        self._set_pipeline(pipeline("image-classification", model=model_id))

    @timed                                # Added elapsed time
    @validate_input((str, Image.Image))  
    def infer(self, data):
        path = data if isinstance(data, str) else getattr(data, "filename", "<PIL Image>")
        self.log("image_infer_start", {"path": path}) # Log the attempt
        key = ("img", path)              # Created the  cache key using image path

        cached = self.get_cache(key)
        if cached:                       # If already cached then return it
            return cached

        img = Image.open(data) if isinstance(data, str) else data  # Open the image when the path is given
        res = self._pipe()(img)[0]       #  pipeline  is run and we get first result
        out = {"label": res["label"], "score": float(res["score"])}
        self.set_cache(key, out)         # Cache result
        return out            

    def info(self) -> str:
        # Description of this model for GUI/info display
        return "Image classification (MobileViT X-Small). Input: image path or PIL Image. Output: label + score."