#!/usr/bin/env python3
""" 3-lru_cache.py """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Constructor method """
        super().__init__()  # Call the parent class constructor
        self.lru_order = []  # Data structure to store the order of cache usage

    def put(self, key, item):
        """
        Add key/value pair to cache data
        If the cache exceeds its max size, remove the least recently used item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item  # Add the key/value pair to the cache

        self.lru_order.append(key)  # Track the order of item usage

    def get(self, key):
        """
        Get the value associated with the given key from the cache
        If the key does not exist in the cache, return None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
