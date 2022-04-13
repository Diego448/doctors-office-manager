from fastapi import FastAPI
from db_utils import add, get, get_all, update, delete, get_related
from models import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get('/patient/all')
async def get_patients():
    return get_all('patients')

@app.get('/patient/{patient_id}')
async def get_patient(patient_id: str):
    return get(patient_id, 'patients')

@app.post('/patient/add')
async def add_patient(patient: Patient):
    return add(patient, 'patients')

@app.patch('/patient/update/{patient_id}')
async def update_patient(patient_id: str, patient_update: PatientUpdate):
    return update(patient_id, patient_update, 'patients')

@app.delete('/patient/delete/{patient_id}')
async def delete_patient(patient_id: str):
    return delete(patient_id, 'patients')

@app.get('/appointment/all')
async def get_all_appointments():
    return get_all('appointments')

@app.get('/appointment/{patient_id}')
async def get_appointments(patient_id: str):
    return get_related('patient_id', patient_id, 'appointments')

@app.post('/appointment/add')
async def add_appointment(appointment: Appointment):
    return add(appointment, 'appointments')

@app.put('/appointment/update/{appointment_id}/')
async def update_appointment(appointment_update: AppointmentUpdate, appointment_id):
    return update(appointment_id, appointment_update, 'appointments')

@app.get('/consult/{patient_id}')
async def get_consults(patient_id: str):
    return get_related('patient_id', patient_id, 'consults')

@app.post('/consult/add')
async def add_consult(consult: Consult):
    return add(consult, 'consults')

@app.get('/consult/{consult_id}')
async def get_consult(consult_id: str):
    return get(consult_id, 'consults')

@app.get('/payment/all')
async def get_all_payments():
    return get_all('payments')

@app.get('/payment/{patient_id}')
async def get_payments(patient_id: str):
    return get_related('patient_id', patient_id, 'payments')

@app.post('/payment/add')
async def add_payment(payment: Payment):
    return add(payment, 'payments')