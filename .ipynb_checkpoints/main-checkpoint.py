from enum import Enum
from typing import Optional
from fastapi import FastAPI

"""
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
"""
app = FastAPI()
@app.get("/")
async def root():
    return "Phonebook"

@app.post("/add-user")
async def add_user(firstname: str, lastname: str, phone_number: str, age: Optional[int] = None):
    print(f'Firstname: {firstname}')
    print(f'Lastname : {lastname}')
    print(f'Phone number: {phone_number}')
    if age:
        print(f'Age:{age}')
    return 'user is added'

@app.get("/get-user")
async def get_user(lastname: str):
    return "Jon Snow, 81992128787, 31"


"""
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
"""