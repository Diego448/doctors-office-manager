from fastapi import FastAPI
from db_utils import add, get, get_all, update, delete
from models import User, UserUpdate

app = FastAPI()

@app.get('/user/all')
async def get_all_users():
    return get_all('users')

@app.get('/user/{user_id}')
async def user_get(user_id: str):
    return get(user_id, 'users')

@app.post('/user/add')
async def add_user(user: User):
    return add(user, 'users')

@app.put('/user/edit/{user_id}')
async def user_edit(user_id: str, user_update: UserUpdate):
    return update(user_id, user_update, 'users')

@app.delete('/user/remove/{user_id}')
async def remove_user(user_id: str):
    return delete(user_id, 'users')