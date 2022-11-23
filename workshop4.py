

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import *

app = FastAPI()

TODOLIST = []

class Item(BaseModel):
    ID: int
    Title: str
    State: int 
    DueDate: str
    Description: str


@app.get("/todo")
async def list():
    return TODOLIST

@app.get("/todo/{item_id}")
async def root(item_id):
     index = [i for i,x in enumerate(TODOLIST) if x.id == item_id][0]
     return {"message": (str(TODOLIST[index].id)) + ":" + str(TODOLIST[index].title)}

@app.post("/todo") #post = modifie
async def create_item(item: Item):
     TODOLIST.append(item)
     return item

@app.delete("/todo/{it}")
async def remove_item(it: int):
    TODOLIST.remove([i for i,x in enumerate(TODOLIST) if x.id == it][0])
    return "removed"