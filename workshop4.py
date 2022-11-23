# from datetime import datetime

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# fake_db = {}

# class Item(BaseModel):
#     ID: int
#     Title: str
#     State: int 
#     DueDate: str
#     description: str


# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     return TODOLIST

# @app.get("/todo/{id}")
# async def read_item(id: int):
#     return {"id": id}

# @app.post("/todo/")
# async def create_item(item: Item):
#     return item

# @app.delete("/item/{item_id}")
# async def delete_hero(hero_id: int):
#     with Session(engine) as session:
#         hero = session.get(Hero, hero_id)
#         if not hero:
#             raise HTTPException(status_code=404, detail="Hero not found")
#         session.delete(hero)
#         session.commit()
#         return {"ok": True}

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