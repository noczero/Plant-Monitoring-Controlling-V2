import json
import logging
import pymysql.cursors
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from src.utils import get_prediction, insert_data_to_firebase

logger = logging.getLogger(__name__)

load_dotenv()  # take environment variables from .env.
PLANT_LIST = json.loads(os.getenv('PLANT_LIST'))
MODE = os.getenv('MODE')


# Connect to the database
class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          port=int(os.getenv('MYSQL_PORT')),
                                          user='root',
                                          password=os.getenv('MYSQL_PASSWORD'),
                                          database=os.getenv('MYSQL_DATABASE'),
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def insert_plant_data_to_mysql(self, sensor):
        """
        Insert realtime plant data and prediction status to database
        :param sensor:
        :return:
        """
        prediction_list = []
        input_data_list = []
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record

                # iterate over plant list
                for index, plant_name in enumerate(PLANT_LIST):

                    # get prediction to API service
                    input_data = sensor.get_single_plant_data(plant_name=plant_name, index_plant=index)

                    # check mode
                    if MODE == "TESTING":
                        prediction = get_prediction(input_data=input_data) # hit prediciton to API
                    elif MODE == "TRAINING":
                        # TRAINING MODE
                        prediction = None # set to none

                    prediction_list.append(prediction)
                    
                    status = None
                    if prediction:
                        status = prediction.get('status', None)
                        input_data['status'] = status

                    # insert data to table
                    sql = "INSERT INTO `plant` " \
                          "(`name`, `temperature`, `humidity`, `light_intensity`, `soil_moisture`, `status`) " \
                          "VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql,
                                   (
                                       plant_name,
                                       sensor.temperature,
                                       sensor.humidity,
                                       sensor.light_intensity,
                                       sensor.soil_moisture_list[index],
                                       status
                                   )
                                   )

                    # append input_data for return
                    input_data_list.append(input_data)

                    # display log
                    logger.info(f"-- Data -- Temperature : {sensor.temperature} "
                                f"\t Humidity : {sensor.humidity} "
                                f"\t Light Intensity : {sensor.light_intensity}"
                                f"\t Soil Moisture : {sensor.soil_moisture_list[index]}")
                    logger.info(f"-- Prediction -- \n {prediction}")

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()

        return prediction_list, input_data_list
