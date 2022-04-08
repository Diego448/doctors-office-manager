from fastapi import FastAPI
from db_utils import add, get, get_all, update, delete
from models import User, UserUpdate

app = FastAPI()

@app.get('/user/all')
async def get_users():
    return get_all('users')

@app.get('/user/{user_id}')
async def get_user(user_id: str):
    return get(user_id, 'users')

@app.post('/user/add')
async def add_user(user: User):
    return add(user, 'users')

@app.put('/user/update/{user_id}')
async def update_user(user_id: str, user_update: UserUpdate):
    return update(user_id, user_update, 'users')

@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: str):
    return delete(user_id, 'users')