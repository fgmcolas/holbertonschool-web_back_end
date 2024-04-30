#!/usr/bin/env python3
"""Function that takes two integer arguments <page> and <page_size>"""
from typing import Tuple


def index_range(page, page_size):
    """return start and end"""
    end = page * page_size
    start = end - page_size
    return (start, end)
