""" 
    Title: mongodb_test.py
    Author: Lathan
    Date: 30 August 2022
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

from pymongo import MongoClient
 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech COllection List --")
print(db.list_collection_names())
