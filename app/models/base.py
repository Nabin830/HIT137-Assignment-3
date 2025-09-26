from abc import ABC, abstractmethod  
from typing import Any, Dict          
class LoggingMixin:

    #  simple helper to log message to the console
    def log(self, event: str, detail: Dict[str, Any] | None = None) -> None:
        print(f"[LOG] {event} :: {detail or {}}")

class CachingMixin:
    # Keeps result in the  memory so  that repeated calls are faster
    _cache: dict = {}  

    def get_cache(self, key):
        return self._cache.get(key)   # Return cached value if it is exist

    def set_cache(self, key, value):
        self._cache[key] = value      # Storing new values in the cache

class HFModelBase(ABC):
    def __init__(self, model_id: str):
        self._model_id = model_id     # Save model id 
        self.__pipe = None            #  variable to store  HF pipeline

    def _set_pipeline(self, pipe) -> None:
        self.__pipe = pipe            #  To assign the pipeline once during init

    def _pipe(self):
        if self.__pipe is None:     
            raise RuntimeError("Pipeline not initialized")
        return self.__pipe            # Return the hidden pipeline

    @abstractmethod
    def infer(self, data: Any) -> Dict[str, Any]:
        # All subclasses must implement this method to run predictions
        ...

    @abstractmethod
    def info(self) -> str:
        
        ...