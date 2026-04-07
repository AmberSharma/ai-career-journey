from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is Running"}


@app.get("/log/count")
def count():
    return {"count": 1}

@app.get("/log/error")
def error():
    return {"errors":5}

@app.get("/log/{file_name}")
def log(file_name: str):
    return {"file_name": file_name, "status": "processed"}

