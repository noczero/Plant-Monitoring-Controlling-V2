from fastapi import APIRouter

from api.scheme.model_scheme import PlantModels

router = APIRouter()


@router.post("/prediction", summary="Predicts plant status using Decision Tree trained models")
async def dt_predicts(request: PlantModels):
    return request
