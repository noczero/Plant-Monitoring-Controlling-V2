import json
import logging
import pymysql.cursors
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

load_dotenv()  # take environment variables from .env.
PLANT_LIST = json.loads(os.getenv('PLANT_LIST'))


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
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record

                # iterate over plant list
                for index, plant_name in enumerate(PLANT_LIST):
                    temperature =  sensor.get_temperature()
                    humidity =  sensor.get_humidity()
                    light_intensity = sensor.get_light_intensity()
                    soil_moisture = sensor.get_soils_moisture()[index]

                    sql = "INSERT INTO `plant` (`name`, `temperature`, `humidity`, `light_intensity`, `soil_moisture`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql,
                                   (
                                       plant_name,
                                       temperature,
                                       humidity,
                                       light_intensity,
                                       # sensor.get_soils_moisture()[0] if plant_name == "plant-A" else sensor.get_soils_moisture()[1],
                                       soil_moisture
                                   )
                                   )

                    logger.info(f"-- Data -- Temperature : {temperature} "
                                f"\t Humidity : {humidity} "
                                f"\t Light Intensity : {light_intensity}"
                                f"\t Soil Moisture : {soil_moisture}" )

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
