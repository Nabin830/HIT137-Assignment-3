from transformers import pipeline                     # Import Hugging Face pipeline
from .base import HFModelBase, LoggingMixin, CachingMixin
from app.utils.decorators import timed, validate_input

class SentimentModel(LoggingMixin, CachingMixin, HFModelBase):
    # This class handle the text sentiment analysis

    def __init__(self, model_id: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        super().__init__(model_id)                    # Call base class constructor
        # Createed the Hugging Face pipeline for the sentiment analysis
        self._set_pipeline(pipeline("sentiment-analysis", model=model_id))

    @timed                           
    @validate_input(str)                  # suring input is a string
    def infer(self, data: str):
        self.log("sentiment_infer_start", {"sample": data[:60]})  # Log the attempt
        cache_key = ("sent", data)        # Createed the  cache key using input text
        cached = self.get_cache(cache_key)
        if cached:                        # If result already cached then return it
            return cached

        res = self._pipe()(data)[0]       # Run the pipeline on text 
        out = {"label": res["label"], "score": float(res["score"])}  
        self.set_cache(cache_key, out)    # the result is saved in cache
        return out                       

    def info(self) -> str:
        #  Description of this model for GUI/info display
        return "Sentiment analysis (DistilBERT, SST-2). Input: text. Output: POS/NEG + score."