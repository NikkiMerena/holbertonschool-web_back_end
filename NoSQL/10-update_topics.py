#!/usr/bin/env python3
"""Changes all topics of a school documnet based on the name"""
import pymongo


def upate_topics(mongo_collection, name, topics):
    """changes all topics of a school doc based on the name"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
