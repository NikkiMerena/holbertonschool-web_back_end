#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union
import functools

class Cache:
    """
    A class for interacting with Redis as a cache.
    """
    def __init__(self):
        """
        Initialize the Cache object and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated random key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve data from.
            fn (callable, optional): A callable function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float]: The retrieved data with optional conversion applied.
        """
        value = self._redis.get(key)

        if value is None:
            return None

        if fn is not None:
            return fn(value)
        else:
            return value

    def get_str(self, key):
        """
        Retrieve data from Redis and decode it as a UTF-8 string.

        Args:
            key (str): The key to retrieve data from.

        Returns:
            str: The retrieved data as a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve data from.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, fn=int)

    @staticmethod
    def count_calls(method):
        """
        A decorator to count the number of times a method is called.

        Args:
            method (callable): The method to be decorated.

        Returns:
            callable: The decorated method.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            method_name = method.__qualname__

            count_key = f"call_count:{method_name}"
            self._redis.incr(count_key)  # Increment the call count

            result = method(self, *args, **kwargs)

            print(f"{method_name} was called {self._redis.get(count_key)} times")  # Print call count
            return result

        return wrapper

# Example usage:
if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
