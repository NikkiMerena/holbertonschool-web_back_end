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


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
