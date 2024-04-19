
from typing import Optional
from fastapi import FastAPI
import pandas as pd
import json
from model import *

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
async def add_user(parameters: User):
    #Считываем/создаём телефонный справочник
    try:
        df_phonebook = pd.read_csv('db.csv')
    except:
        df_phonebook = pd.DataFrame(columns=['Firstname', 'Lastname', 'Phone number', 'Age'])#создание "колонок"
        df_phonebook['Phone number'] = df_phonebook['Phone number'].astype(str)

    user_dict = {}
    user_dict['Firstname'] = parameters.firstname
    user_dict['Lastname'] = parameters.lastname
    user_dict['Phone number'] = parameters.phone_number

    print(f'Firstname: {parameters.firstname}')
    print(f'Lastname : {parameters.lastname}')
    print(f'Phone number: {parameters.phone_number}')
    if parameters.age:
        print(f'Age:{parameters.age}')
        user_dict['Age'] = parameters.age
    else:
        user_dict['Age'] = 'None'

    print(user_dict)
    df_temp = pd.DataFrame([user_dict])
    print(df_phonebook)
    print(df_temp)
    df_phonebook = pd.concat([df_phonebook, df_temp])
    df_phonebook.to_csv('db.csv')
    return 'user is added'






@app.get("/get-user")
async def get_user(lastname: str):
    try:
        df_phonebook = pd.read_csv('db.csv')
    except:
        df_phonebook = pd.DataFrame(columns=['Firstname', 'Lastname', 'Phone number', 'Age'])  # создание "колонок"
        df_phonebook['Phone number'] = df_phonebook['Phone number'].astype(str)
    df_temp = df_phonebook[df_phonebook['Lastname'] == lastname]
    if df_temp.empty:
        return 'There is no such user'
    print(dict(df_temp.iloc[0]))
    return json.dumps(dict({'Phone number': df_temp.iloc[0]['Phone number']}))


"""
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
"""