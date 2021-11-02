import logging

logger = logging.getLogger(__name__)


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
        self.dht22 = None
        self.bh1750 = None
        self.relay = None
        self.ads1155 = None
        pass

    def get_temperature(self):
        logger.debug("Get temperature")
        return 1.0

    def get_humidity(self):
        logger.debug("Get Humidity")
        return 11.0

    def get_soils_moisture(self):
        logger.debug("Get Soil Moisture")
        return [1, 1]

    def get_light_intensity(self):
        logger.debug("Get Light Intensity")
        return 1.0

    def control_relay(self):
        logger.debug("Control Relay")
        return True


