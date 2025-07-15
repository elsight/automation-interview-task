from mongomock import MongoClient

client = MongoClient()
db = client["test_db"]
devices_collection = db["devices"]

# After creating the devices_collection
devices_collection.create_index("ip_address", unique=True)