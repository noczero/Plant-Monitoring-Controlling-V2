from dotenv import load_dotenv
import os
import requests

load_dotenv()  # take environment variables from .env.

MAX_VALUE_ADS = 32767

BASE_URL_API = f"http://localhost:{os.getenv('API_PORT')}/v1" # set API URL
URL_API = f"{BASE_URL_API}/{os.getenv('MODEL_NAME')}"


def _map(x, min_input, max_input, min_output, max_output):
    """
    Map value between range
    """
    return ((MAX_VALUE_ADS - x) - min_input) * (max_output - min_output) / (max_input - min_input) + min_output


def discrete_soil_reading(raw_analog):
    """
    Convert RAW Analog to discrete (low, normal, high) for soil moist level
    :param raw_analog: 0-MAX_VALUE_ADS
    :return: String moist level
    """
    status = None

    percentage = _map(raw_analog, 0, MAX_VALUE_ADS, 0, 100)

    # range of soil moist level, based on percentage
    if 25 < percentage <= 100:
        status = "High"
    elif 15 <= percentage <= 25:
        status = "Normal"
    elif 0 <= percentage < 15:
        status = "Low"

    return status


def get_prediction(input_data: dict):
    """
    Do post request to API service that handle model prediction
    :param input_data: dictionary with this schema {
        "name": "Bayam",
        "temperature": 33,
        "humidity": 40,
        "light_intensity": 100,
        "soil_moisture": "HIGH"
    }
    :return: a dictionary with this schema {
          "name": "Bayam",
          "temperature": 33,
          "humidity": 40,
          "light_intensity": 100,
          "soil_moisture": "HIGH",
          "soil_moisture_encode": 100,
          "status": "Optimal"
        }
    """

    url = f"{URL_API}/prediction"
    response = requests.post(url, json=input_data)
    if response.status_code != 200:
        return None
    else:
        return response.json()


def is_need_for_watering(prediction_list: [dict]):
    """
    Compare status in prediction list if any not optimal then return True
    :param prediction_list:
    :return:
    """
    for prediction in prediction_list:
        if prediction:
            if prediction.get('status', '') == "Not Optimal":
                return True

    return False
