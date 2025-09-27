class BaseTask:
    
    def __init__(self):
        self._last_result = None  # encapsulated state

    def run(self, data):
        raise NotImplementedError("Subclasses must override run()")

    def get_last_result(self):
        return self._last_result

    def _set_last_result(self, value):
        self._last_result = value
