import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from my_app.routers import web 


app = FastAPI()
app.mount("/static", StaticFiles(directory="my_app/static"), name="static")

app.include_router(web.router)
