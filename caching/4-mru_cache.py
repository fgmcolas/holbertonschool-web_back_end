#!/usr/bin/python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

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
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

        if key not in self.order:
            self.order.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """Gets item by key"""
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """Move element to last idx"""
        length = len(self.order)
        if self.order[length - 1] != item:
            self.order.remove(item)
            self.order.append(item)
