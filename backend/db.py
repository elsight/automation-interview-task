from mongomock import MongoClient

client = MongoClient()
db = client["test_db"]
devices_collection = db["devices"]