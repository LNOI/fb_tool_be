import json
from datetime import datetime, timedelta
from functools import wraps
from uuid import UUID
import redis
from typing import Any

r = redis.Redis(host="localhost", port=6379, db=0)


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        elif isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, obj)


# cache api with arguments expiring time 30s
def cache_api(ex: int = 30):
    def wrapper(func):
        @wraps(func)
        async def wrap(*args, **kwargs):
            key = f"{func.__name__}"
            for k, v in kwargs.items():
                if k not in ["db", "s", "limit"]:
                    key += f"-{k}_{v}"
            if r.exists(key):
                return json.loads(r.get(key))

            result = await func(*args, **kwargs)
            r.set(key, json.dumps(result, cls=UUIDEncoder), ex=ex)
            return result

        return wrap

    return wrapper


def set_cache(key: str, value: Any, ex: float = 3600) -> None:
    r.set(key, json.dumps(value), ex=timedelta(seconds=ex))


def get_cache(key: str) -> str | None:
    v = r.get(key)
    if v:
        return json.loads(v)
    return None


def delete_cache(key) -> None:
    r.delete(key)
