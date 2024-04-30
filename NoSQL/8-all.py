#!/usr/bin/env python3
"""Function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
