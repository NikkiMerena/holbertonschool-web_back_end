#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class to interact with Redis
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
        # Retrieve the value from Redis using self._redis.get(key)
        value = self._redis.get(key)

        if value is None:
            return None

        # Apply the provided Callable (fn) if available
        if fn is not None:
            return fn(value)
        else:
            return value  # Return the value as-is if fn is not provided

    def get_str(self, key):
        # Use get method with fn to decode as UTF-8 string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        # Use get method with fn to convert to int
        return self.get(key, fn=int)

# Example usage:
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value


if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
