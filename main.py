from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def foo():
    return 'hello world'