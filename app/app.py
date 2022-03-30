import logging.config
import os
from time import sleep
import RPi.GPIO as GPIO

from src.utils import is_need_for_watering, insert_data_to_firebase
from src.sensors import Sensor
from db.connection import Database
from dotenv import load_dotenv
import os
import json

load_dotenv()  # take environment variables from .env.

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Plant Monitoring and Controlling Apps is starting...")

    try:
        while True:
            # create sensor object
            my_sensor = Sensor()

            # create database object
            my_db = Database()

            # reading all sensor data
            my_sensor.reading_all_sensors()

            # insert data to database
            result, input_data_list = my_db.insert_plant_data_to_mysql(my_sensor)

            # insert to firebase
            insert_data_to_firebase(input_data_list=input_data_list)

            # check for watering
            if is_need_for_watering(result):
                my_sensor.control_relay("ON")
                sleep(10)  # 10s ON
                my_sensor.control_relay("OFF")

            sleep(60)  # 1 minutes


    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
    finally:
        GPIO.cleanup()
