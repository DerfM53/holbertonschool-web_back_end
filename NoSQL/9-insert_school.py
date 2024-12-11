#!/usr/bin/env python3
"""This module contain a function"""


def insert_school(mongo_collection, **kwargs):
    """
    This function take an variable arguments and insert
    into database
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
