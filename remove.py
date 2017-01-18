#!/usr/bin/env python
import json
import pymongo
import hashlib 
from pymongo import MongoClient
client=MongoClient()
client =MongoClient('mongodb://')
db=client.links 
collection=db.toi_feed
ta=db.fdetect
# results=ta.delete_many({})