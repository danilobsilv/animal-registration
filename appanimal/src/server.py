from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)


class Animal(BaseModel):
    id: Optional[str]
    name: str
    idade: int
    sex: str
    color: str


db: List[Animal] = []


@app.get('/animals')
def list_animals():
    return db


@app.get('/animals/{animal_id}')
def get_animal(animal_id: str):
    for animal in db:
        if animal.id == animal_id:
            return animal
    return {'ERROR': 'Animal not found'}


@app.delete('/animals/{animal_id}')
def delete_animal(animal_id: str = Path(..., title="animal's code to look for")):
    position = -1
    for index, animal in enumerate(db):
        if animal.id == animal_id:
            position = index
            break

    if position != -1:
        db.pop(position)
        return {'message': 'Animal deleted successfully'}
    else:
        return {'ERROR': 'Animal not found'}


@app.post('/animals')
def create_animal(animal: Animal):
    animal.id = str(uuid4())
    db.append(animal)
    return None
