from fastapi import APIRouter

from api.scheme.model_scheme import PlantModels
from api.utils.helpers import KNN

router = APIRouter()


@router.post("/prediction", summary="Predicts plant status using K-Nearest Neighbor trained models")
async def knn_predicts(request: PlantModels):
    trained_knn = KNN(plant=request)
    request.status = trained_knn.get_prediction()
    return request
