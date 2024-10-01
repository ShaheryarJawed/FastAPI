from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"}

@app.get("/age/{age}")
def show_age(age: int):
    return {"age": age}
