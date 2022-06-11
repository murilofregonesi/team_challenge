from functools import wraps
import time


def execution_time(func):
    """Decorator to print execution time is seconds."""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        init_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f'- Execution time: {func.__name__} - {end_time - init_time}s')
        return result

    return wrapper
