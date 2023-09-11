#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class
    This class inherits from BaseCaching and is a caching system that
    implements the FIFO algorithm.
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key (str): key of the item.
            item (str): item to add in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        Args:
            key (str): key of the item to get.
        Returns:
            item (str): item in the cache linked to the key.
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    pass
