from pymongo import MongoClient
from pymongo.errors import PyMongoError
from models import User, Patient, UserUpdate
from bson import ObjectId, json_util
from typing import Union, Final
import json

try:
    client = MongoClient()
    db = client.doctors_office_management_dev
except PyMongoError as e:
    print(f'An error occured: {e}')

def create_user(user: User) -> dict:
    response = {}
    result = db.users.insert_one(user.dict())
    response['success'] = result.acknowledged
    if result.acknowledged:
        response['inserted_id'] = str(result.inserted_id)
        response['data'] = user
    return response

def get_users() -> list:
    return json.loads(json_util.dumps(db.users.find({})))

def get_user(user_id: str) -> dict:
    return json.loads(json_util.dumps(db.users.find({'_id': ObjectId(user_id)})))

def delete_user(user_id: str) -> dict:
    response = {}
    try:
        result = db.users.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            response['success'] = True
            response['deleted_id'] = user_id
        else:
            response['success'] = False
    except PyMongoError as e:
        response['success'] = False
        response['error'] = e._message
    return response

def update_user(user_id: str, user_update: UserUpdate) -> dict:
    response = {}
    result = db.users.update_one({'_id': ObjectId(user_id)}, {'$set':user_update.dict()})
    if result.acknowledged:
        response['success'] = True
        response['updated_id'] = user_id
    else:
        response['success'] = False
    return response

def get(id: str, collection: str) -> list:
    try:
        response = json.loads(json_util.dumps(db[collection].find({'_id': ObjectId(id)})))
    except PyMongoError as e:
        response = [{'error': e._message}]
    return response

def get_related(field:str, id: str, collection: str) -> list:
    try:
        response = json.loads(json_util.dumps(db[collection].find({field: id})))
        print(collection, field, id)
    except PyMongoError as e:
        response = [{'error': e._message}]
    return response

def get_all(collection: str) -> list:
    try:
        response = json.loads(json_util.dumps(db[collection].find({})))
    except PyMongoError as e:
        response = [{'error': e._message}]
    return response

def add(data: Union[User, Patient], collection: str) -> dict:
    response = {}
    try:
        result = db[collection].insert_one(data.dict())
        response['success'] = result.acknowledged
        if result.acknowledged:
            response['inserted_id'] = str(result.inserted_id)
            response['data'] = data
    except PyMongoError as e:
        response['success'] = False
        response['error'] = e._message
    return response

def delete(id: str, collection: str) -> dict:
    response = {}
    try:
        result = db[collection].delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 1:
            response['success'] = True
            response['deleted_id'] = id
        else:
            response['success'] = False
    except PyMongoError as e:
        response['success'] = False
        response['error'] = e._message
    return response

def update(id: str, update_data: Union[UserUpdate, Patient], collection: str) -> dict:
    response = {}
    try:
        result = db[collection].update_one({'_id': ObjectId(id)}, {'$set':update_data.dict()})
        if result.acknowledged:
            response['success'] = True
            response['updated_id'] = id
        else:
            response['success'] = False
    except PyMongoError as e:
        response['success'] = False
        response['error'] = e._message
    return response