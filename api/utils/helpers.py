import pickle

from fastapi.logger import logger

from api.scheme.model_scheme import PlantModels

MAP_SOIL_MOIST_ENCODE = {
    "Low": 0,
    "Normal": 50,
    "High": 100
}


class TrainedModels:
    def __init__(self, plant: PlantModels):
        self.plant_models = plant
        self.trained_model = None
        # set encode based on soil moisture
        if plant.soil_moisture:
            self.plant_models.soil_moisture_encode = MAP_SOIL_MOIST_ENCODE[plant.soil_moisture.capitalize()]


class KNN(TrainedModels):
    def __init__(self, plant: PlantModels):
        super().__init__(plant)

        if 'bayam' in plant.name.lower():
            # load bayam models
            self.trained_model = pickle.load(open('api/trained/bayam_knn_model.sav', 'rb'))

        elif 'caisim' in plant.name.lower():
            # load caisim models
            self.trained_model = pickle.load(open('api/trained/caisim_knn_model.sav', 'rb'))
        else:
            logger.warn("Type of plant doesn't support yet")

    def get_prediction(self):
        test_features = [self.plant_models.temperature,
                         self.plant_models.humidity,
                         self.plant_models.light_intensity,
                         self.plant_models.soil_moisture_encode]

        return self.trained_model.predict([test_features])[0]


class DecisionTree(TrainedModels):
    def __init__(self, plant: PlantModels):
        super().__init__(plant)

        if 'kale' in plant.name.lower() :
            # load kale models
            self.trained_model = pickle.load(open('api/trained/kale_dt_model.sav', 'rb'))

        elif 'seledri' in plant.name.lower() :
            # load seledri models
            self.trained_model = pickle.load(open('api/trained/seledri_dt_model.sav', 'rb'))
        else:
            logger.warn("Type of plant doesn't support yet")

    def get_prediction(self):
        test_features = [self.plant_models.temperature,
                         self.plant_models.humidity,
                         self.plant_models.light_intensity,
                         self.plant_models.soil_moisture_encode]

        return self.trained_model.predict([test_features])[0]