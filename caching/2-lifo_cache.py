#!/usr/bin/python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item in cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.order:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        if key not in self.order:
            self.order.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """Gets item by key"""
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """Move element to last idx"""
        length = len(self.order)
        if self.order[length - 1] != item:
            self.order.remove(item)
            self.order.append(item)
