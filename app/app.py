import logging.config
import os
from time import sleep
import RPi.GPIO as GPIO
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
    #my_sensor = Sensor()
    #my_db = Database()
    #my_db.insert_plant_data_to_mysql(my_sensor)
    #GPIO.cleanup()

    try:
         while True:
             my_sensor = Sensor()
             my_db = Database()
             my_db.insert_plant_data_to_mysql(my_sensor)
             sleep(60) # 1 minutes

    except KeyboardInterrupt:
         print("Press Ctrl-C to terminate while statement")
         pass
    finally:
         GPIO.cleanup()

