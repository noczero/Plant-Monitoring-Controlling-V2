from fastapi import APIRouter

from api.router import dt_endpoint, knn_endpoint

api_router = APIRouter()

api_router.include_router(dt_endpoint.router, prefix="/decision-tree", tags=["Decision Tree"])
api_router.include_router(knn_endpoint.router, prefix="/knn", tags=["K-Nearest Neighbor"])
