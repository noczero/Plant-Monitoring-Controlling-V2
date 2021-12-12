from fastapi import APIRouter

from api.scheme.model_scheme import PlantModels
from api.utils.helpers import DecisionTree

router = APIRouter()


@router.post("/prediction", summary="Predicts plant status using Decision Tree trained models")
async def dt_predicts(request: PlantModels):
    trained_dt = DecisionTree(plant=request)
    request.status = trained_dt.get_prediction()
    return request
