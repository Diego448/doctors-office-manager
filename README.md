# DOOFMAN
## Doctor's Office Manager

DOOFMAN is a simple doctor's office management system for small bussines that allows you to easily keep track of medical appointments and clinic history although with managing payments and patient information

### Project setup
#### Backend
* Install **Python 3.10**. `sudo apt-get install python3.10`
* Navigate to backend folder. `cd backend`
* Create a virtual environment inside backend folder. `python3.10 -m venv .`
* Activate your virtual environment. `source bin/activate`
* Install required packages inside the virtual environment. `pip install -r requirements.txt`
* Navigate to source files folder. `cd src/doofman`
* Start **uvicorn** server in development mode. `uvicorn app:app --reload`