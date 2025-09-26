import time                    
from functools import wraps    

def timed(fn):
    # This decorator  measure how long a function take to run  and add  elapsed time 
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t = time.time()        #  start time is recoreded
        out = fn(*args, **kwargs)   #functons runs here
        if isinstance(out, dict):  
            out["_elapsed_sec"] = round(time.time() - t, 3)
        return out              # Return the result 
    return wrapper              #

def validate_input(expected_types):
    #  checking  that the input to a function
    def deco(fn):
        @wraps(fn)
        def wrapper(self, data, *args, **kwargs):
            if not isinstance(data, expected_types):   #  input type is checked
                raise TypeError(f"Expected {expected_types}, got {type(data)}")
            return fn(self, data, *args, **kwargs)    # runing the function
        return wrapper
    return deco