from fastapi import FastAPI
from typing import Optional, Literal
from pydantic import BaseModel
import json as js

class Whey(BaseModel):
    name: str
    qty: Optional[int] = 20
    price: int
    brand: Literal['Whey Protein', 'Creatine', 'Pre Workout', 'Post Workout'] = 'us'


app = FastAPI()

@app.get('/fruits')
def post_method_example():
    return {"Name":"Pradyumna","Age":20}

@app.get('/ReadJson')
def read_json():
    with open('three.json', 'r') as file:
        data = js.load(file)
    print(data)
    return data
