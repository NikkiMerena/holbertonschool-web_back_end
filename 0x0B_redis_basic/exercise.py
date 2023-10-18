#!/usr/bin/env python3
""" Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

# Constants for Redis keys
INPUTS_KEY = ":inputs"
OUTPUTS_KEY = ":outputs"

def count_calls(method: Callable) -> Callable:
    """ Count the number of times a method is called. """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs for a particular function. """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Store the input
        self._redis.rpush(f"{method.__qualname__}{INPUTS_KEY}", str(args))
        # Compute the output
        output = method(self, *args, **kwargs)
        # Store the output
        self._redis.rpush(f"{method.__qualname__}{OUTPUTS_KEY}", output)
        return output
    return wrapper

def replay(method: Callable):
    """ Display the history of calls of a particular function. """
    r = redis.Redis()
    name = method.__qualname__
    count = r.get(name).decode("utf-8")
    inputs = r.lrange(f"{name}{INPUTS_KEY}", 0, -1)
    outputs = r.lrange(f"{name}{OUTPUTS_KEY}", 0, -1)
    print(f"{name} was called {count} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{name}(*{input_data.decode('utf-8')}) -> {output_data.decode('utf-8')}")

class Cache:
    """ Cache class. """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store the input data in Redis using a randomly generated key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Convert the data back to the desired format. """
        data = self._redis.get(key)
        if not data:
            return None
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ Convert bytes to string. """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: bytes) -> int:
        """ Convert bytes to int. """
        return self.get(key, fn=lambda x: int(x.decode("utf-8")))

# Usage example
if __name__ == '__main__':
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
