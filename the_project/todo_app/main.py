import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    port = os.getenv("PORT", 8000)
    return {"message": f"Hello, World! The server is running on port {port}."}