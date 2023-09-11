#!/usr/bin/env python3
""" 0-basic_cache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    This class inherits from BaseCaching and is a basic caching system.
    The caching system doesn't have a limit.
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key (str): key of the item.
            item (str): item to add in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key (str): key of the item to get.
        Returns:
            item (str): item in the cache linked to the key.
        """
        return self.cache_data.get(key, None)
