from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from uuid import uuid4
from datetime import datetime
from .db import devices_collection
from .redis_client import redis_client
from .models import Device
import json
import os


app = FastAPI()

# Mount the frontend directory
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')

@app.get("/api/devices")
def list_devices():
    cache = redis_client.get("devices")
    if cache:
        return json.loads(cache)
    # Get devices and ensure IP addresses are strings
    devices = list(devices_collection.find({}, {'_id': 0}))
    # Ensure all documents have string IP addresses
    for device in devices:
        if 'ip_address' in device:
            device['ip_address'] = str(device['ip_address'])
    redis_client.set("devices", json.dumps(devices))
    return devices

@app.post("/api/device")
def create_device(device: Device):
    device_data = device.model_dump()  # Use model_dump() instead of dict()
    device_data['ip_address'] = str(device_data['ip_address'])  # Convert IP to string
    device_data.update({
        "id": str(uuid4()),
        "status": "offline",
        "last_updated": datetime.utcnow().isoformat()
    })
    devices_collection.insert_one(device_data)
    redis_client.delete("devices")
    return device_data

@app.put("/api/device/{device_id}")
def update_device(device_id: str, device: Device):
    update_data = device.model_dump()  # Use model_dump() instead of dict()
    update_data['ip_address'] = str(update_data['ip_address'])  # Convert IP to string
    update_data["last_updated"] = datetime.utcnow().isoformat()
    result = devices_collection.update_one({"id": device_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Device not found")
    redis_client.delete("devices")
    updated_device = devices_collection.find_one({"id": device_id}, {'_id': 0})
    return updated_device

@app.delete("/api/device/{device_id}")
def delete_device(device_id: str):
    result = devices_collection.delete_one({"id": device_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Device not found")
    redis_client.delete("devices")
    return {"status": "deleted"}