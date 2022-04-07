from fastapi import FastAPI
from db_utils import delete_user, get_users, create_user, get_user, update_user, add, get, get_all, update
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
    return delete_user(user_id)