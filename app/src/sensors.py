import json
import logging
# Import the ADS1x15 module.
import os
import Adafruit_ADS1x15
import board
import adafruit_bh1750
import Adafruit_DHT
import RPi.GPIO as GPIO
from dotenv import load_dotenv

from .utils import discrete_soil_reading

load_dotenv()  # take environment variables from .env.
GPIO.setmode(GPIO.BCM)

logger = logging.getLogger(__name__)

i2c = board.I2C()

# relay as output
GPIO.setup(int(os.getenv('RELAY_PIN')), GPIO.OUT)  # relay
GPIO.output(int(os.getenv('RELAY_PIN')), GPIO.HIGH)  # set as OFF

PLANT_LIST = json.loads(os.getenv('PLANT_LIST'))


class Sensor:
    """
    This class provides object from several sensor,
    1. DHT22 : humidiy
    2. BH1760 : Light intensity I2C board
    4. ADS1155 : ADC module I2C board
    3. Relay : Watering control

    @note :
    Using the sensor
    """

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.soil_moisture_list = None
        self.light_intensity = None
        self.dht22 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, int(os.getenv('DHT22_PIN')))
        self.bh1750 = adafruit_bh1750.BH1750(i2c)
        self.ads1155 = Adafruit_ADS1x15.ADS1115(address=0x48)
        self.ads1155_second = Adafruit_ADS1x15.ADS1115(address=0x4a)

    def get_temperature(self):
        logger.debug("Get temperature")
        self.temperature = self.dht22[1]
        return self.dht22[1]

    def get_humidity(self):
        logger.debug("Get Humidity")
        self.humidity = self.dht22[0]
        return self.dht22[0]

    def get_soils_moisture(self):
        logger.debug("Get Soil Moisture")

        # read from ads1155 based on plant number set in .env, max [4]
        adc_list = [0] * len(PLANT_LIST)
        discrete_value = [''] * len(PLANT_LIST)  # make empty string array
        for i in range(len(PLANT_LIST)):
            logger.debug(f"index : {i}")

            if i < 4:
                # i = 0 - 3
                # get value from first ads1155 with gain 2
                adc_value = self.ads1155.read_adc(i, gain=2)
            elif i < 8:
                # i = 4 - 7
                # get value from second ads1115
                adc_value = self.ads1155_second.read_adc((i - 4), gain=2)
            else:
                logger.error("PLANT LIST out of range sensor ADS1155")

            logger.debug(f"ADC Values : {adc_value}")

            # convert to discreate value
            discrete_value[i] = discrete_soil_reading(raw_analog=adc_value)  # set value to LOW, NORMAL, or HIGH

        self.soil_moisture_list = discrete_value
        return discrete_value

    def get_light_intensity(self):
        logger.debug("Get Light Intensity")
        self.light_intensity = self.bh1750.lux
        return self.bh1750.lux

    def control_relay(self, command):
        logger.debug("Control Relay")
        if command == "ON":
            logger.info("Watering ON")
            GPIO.output(int(os.getenv('RELAY_PIN')), GPIO.LOW)
        elif command == "OFF":
            logger.info("Watering OFF")
            GPIO.output(int(os.getenv('RELAY_PIN')), GPIO.HIGH)
        else:
            logger.error("Invalid command")

        return True

    def reading_all_sensors(self):
        self.get_temperature()
        self.get_humidity()
        self.get_soils_moisture()
        self.get_light_intensity()

    def get_single_plant_data(self, plant_name, index_plant):
        return {
            "name": plant_name,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "light_intensity": self.light_intensity,
            "soil_moisture": self.soil_moisture_list[index_plant]
        }
