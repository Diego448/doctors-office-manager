from fastapi import FastAPI
from db_utils import delete_user, get_users, create_user, get_user, update_user, add
from models import User, UserUpdate

app = FastAPI()

@app.get('/user/all')
async def get_all_users():
    return get_users()

@app.get('/user/{user_id}')
async def user_get(user_id: str):
    return get_user(user_id)

@app.post('/user/add')
async def add_user(user: User):
    return create_user(user)

@app.put('/user/edit/{user_id}')
async def user_edit(user_id: str, user_update: UserUpdate):
    return update_user(user_id, user_update)

@app.delete('/user/remove/{user_id}')
async def remove_user(user_id: str):
    return delete_user(user_id)

@app.post('/test/add')
async def test_add(user: User):
    return add(user, 'users')