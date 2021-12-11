from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.router import api_router
from api.scheme.model_scheme import PlantModels


app = FastAPI(
    version="1.0.0",
    title="Plant Monitoring and Controlling",
    description="This API provides classification result using KNN and Decision Tree",
    docs_url="/",
    openapi_url="/v1/openapi.json")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/v1")
