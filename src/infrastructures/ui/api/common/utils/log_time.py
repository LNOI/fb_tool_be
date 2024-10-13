import time
from functools import wraps


def log_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        response = await func(*args, **kwargs)
        end_time = time.time()
        return response

    return wrapper
