from fastapi import FastAPI
from db_utils import get_users, create_user
from models import User

app = FastAPI()

@app.get('/user/all')
async def get_all_users():
    return get_users()

@app.post('/user/add')
async def add_user(user: User):
    return create_user(user)