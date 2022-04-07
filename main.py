from fastapi import FastAPI

app = FastAPI()


@app.get("/locators")
async def locators():
    return {"message": "save locators"}


@app.get("/")
async def root():
    return {"message": "Hello World"}