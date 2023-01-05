from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .data.db_utils import initialize_app


app = FastAPI(title="Infirmier A Domicile")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", initialize_app)

@app.get("/")
async def root():
    return {"message": "Hello World"}
