from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Backend is running!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/api/status")
def status():
    return {
        "status": "Healthy",
        "version": "1.0.0",
        "random_number": random.randint(1, 100)
    }


@app.get("/api/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}!"
    }