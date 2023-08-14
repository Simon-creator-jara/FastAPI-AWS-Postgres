from fastapi import FastAPI
from resources.routes import api_router
from db import database
from fastapi.middleware.cors import CORSMiddleware

origins=[
    "http://localhost",
    "http://localhost:8000"
]

app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
