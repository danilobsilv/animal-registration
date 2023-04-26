from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[str]
    name: str
    age: int
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
def delete_animal(animal_id: str):
    position = -1
    # buscar o position do animal
    for index, animal in enumerate(db):
        if animal.id == animal_id:
            position = index
            break

    if position != -1:
        db.pop(position)
        return {'message': 'Animal removed successfully'}
    else:
        return {'ERROR': 'Animal not found'}


@app.post('/animals')
def create_animal(animal: Animal):
    animal.id = str(uuid4())
    db.append(animal)
    return None
