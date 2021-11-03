import logging
# Import the ADS1x15 module.
import os
import Adafruit_ADS1x15
import board
import adafruit_bh1750
import Adafruit_DHT
import RPi.GPIO as GPIO
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
GPIO.setmode(GPIO.BCM)

logger = logging.getLogger(__name__)

i2c = board.I2C()
# relay as output
GPIO.setup(int(os.getenv('RELAY_PIN')), GPIO.OUT)  # relay

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
        self.dht22 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, int(os.getenv('DHT22_PIN')))
        self.bh1750 = adafruit_bh1750.BH1750(i2c)
        self.ads1155 = Adafruit_ADS1x15.ADS1115()

    def get_temperature(self):
        logger.debug("Get temperature")
        return self.dht22[1]

    def get_humidity(self):
        logger.debug("Get Humidity")
        return self.dht22[0]

    def get_soils_moisture(self):
        logger.debug("Get Soil Moisture")
        adc_list = [0]*2
        for i in range(2):
            adc_list[i] = self.ads1155.read_adc(i, gain=1)
        return adc_list

    def get_light_intensity(self):
        logger.debug("Get Light Intensity")
        return self.bh1750.lux

    def control_relay(self, command):
        logger.debug("Control Relay")
        if command == "ON":
            logger.info("Watering ON")
            GPIO.output(os.getenv('RELAY_PIN'), GPIO.LOW)
        elif command == "OFF":
            logger.info("Watering OFF")
            GPIO.output(os.getenv('RELAY_PIN'), GPIO.HIGH)
        else:
            logger.error("Invalid command")

        return True


