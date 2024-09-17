#!/usr/bin/python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item in cache"""
        if key is None or item is None:
            return

        if key not in self.order:
            self.order.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.get_first_list(self.order)
            if oldest_key:
                self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Gets item by key"""
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """Move element to last idx"""
        length = len(self.order)
        if self.order[length - 1] != item:
            self.order.remove(item)
            self.order.append(item)

    @staticmethod
    def get_first_list(array):
        """Get first element of the list"""
        return array[0] if array else None
