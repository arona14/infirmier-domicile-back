from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from .nurse import nurse_routes

from .data.db_utils import initialize_app


app = FastAPI(title="Infirmier A Domicile")

api_router = APIRouter()
api_router.include_router(nurse_routes.router, prefix="/infirmiers", tags=["Infirmiers"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", initialize_app)
app.include_router(api_router, prefix='/api')

