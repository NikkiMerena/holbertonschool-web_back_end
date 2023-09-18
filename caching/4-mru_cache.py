#!/usr/bin/env python3
""" 4-mru_cache.py """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """Assign to dictionary self.cache_data item value for the key key"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                print(f"DISCARD: {self.mru_key}")
                self.cache_data.pop(self.mru_key)
        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.mru_key = key
        return self.cache_data.get(key)
