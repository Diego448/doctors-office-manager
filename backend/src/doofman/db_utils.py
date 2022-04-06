from pymongo import MongoClient
from models import User
from bson import ObjectId, json_util
import json

client = MongoClient()

db = client.doctors_office_management_dev

def create_user(user: User) -> dict:
    response = {}
    result = db.users.insert_one(user.dict())
    response['success'] = result.acknowledged
    if result.acknowledged:
        response['inserted_id'] = str(result.inserted_id)
        response['data'] = user
    return response

def get_users():
    return json.loads(json_util.dumps(db.users.find({})))

def delete_user(user_id: str):
    response = {}
    result = db.users.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        response['success'] = True
        response['deleted_id'] = user_id
    else:
        response['success'] = False
    return response