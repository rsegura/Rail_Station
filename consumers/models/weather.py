"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info(f"weather event: {message.value()}")
        weather_data = message.value()
        self.temperature = weather_data['temperature']
        self.status = weather_data['status']
        #json_value = json.loads(message.value())
        #try:
        #    self.temperature = json_value['temperature']
        #    self.status = json_value['status']
        #except KeyError as err:
        #    logger.error(f"error reading message: {err.message}")