from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def greeting(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/greeting/{name}")
def greeting_path(name: str, age: Optional[int] = None):
    return {"message": f"Hello, {name}! You are {age} years old."}
