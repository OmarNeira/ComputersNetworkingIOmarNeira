#Imports
from email import message
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def healthCheck():
    return {"status": "I am allive"}

@api.get("/hello_UD")
def hello_ud():
    message = {"date": "2021-09-01",
               "message": "Hello UD Students",
               "class": "Computer Networking"}
    return message