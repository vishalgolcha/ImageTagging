#!/usr/bin/env python
import json
import pymongo
import hashlib 
from pymongo import MongoClient
client=MongoClient()
client =MongoClient('mongodb://digi1:digi1234@52.21.107.21:27017')
db=client.links 
collection=db.toi_feed
ta=db.fdetect
# results=ta.delete_many({})