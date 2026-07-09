from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Bio(BaseModel):
    age : int 
    name : str

data : list[Bio] = []


@app.get("/")
def root_path():
    return {"message":"This is my first API call usage"}

@app.post("/bio")
def get_info(bio : Bio):
    data.append(bio)
    return data
