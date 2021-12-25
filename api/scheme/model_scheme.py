from typing import Optional

from pydantic import BaseModel, validator

'temperature', 'humidity', 'light_intensity', 'soil_moisture_encode'


class PlantModels(BaseModel):
    name: Optional[str]
    temperature: Optional[float]
    humidity: Optional[float]
    light_intensity: Optional[float]
    soil_moisture: Optional[str]
    soil_moisture_encode: Optional[float]
    status: Optional[str]

    class Config:
        orm_mode = True,
        validate_assignment = True
        schema_extra = {
            "example" : {
                "name" : "Bayam",
                "temperature": 33,
                "humidity": 40,
                "light_intensity": 100,
                "soil_moisture": "High"
            }
        }
