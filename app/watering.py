import json
import os

import requests
from dotenv import load_dotenv

from src.utils import get_prediction


load_dotenv()  # take environment variables from .env.
BASE_URL_API = f"http://localhost:{os.getenv('API_PORT')}/v1"
URL_API = f"{BASE_URL_API}/{os.getenv('MODEL_NAME')}"


def test_prediction(input_data: json):

    url = f"{URL_API}/prediction"
    r = requests.post(url, json=input_data)

    print(r.json())


if __name__ == '__main__':
    input_data = {
        "name": "Bayam",
        "temperature": 33,
        "humidity": 40,
        "light_intensity": 100,
        "soil_moisture": "HIGH"
    }

    test_prediction(input_data)

    print(get_prediction(input_data))