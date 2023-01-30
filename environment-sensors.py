# Team: Pi
# CPSC 341
# Dr.Zhang
# 30 January 2023
# Assignment Desc: Sense the local environment and output the data

from sense_hat import SenseHat
from time import sleep

class EnvironmentData():
    def __init__(self) -> None:
        pass

    def getTemperature(self,sense):
        temperature = sense.get_temperature() # get temperature
        sense.show_message("Temperature: ")
        sense.show_message(str(round(temperature,2))) # display
        sleep(2)
    
    def getHumidity(self, sense):
        humidity = sense.get_humidity() # get humidity
        sense.show_message("Humidity: ")
        sense.show_message(str(round(humidity,2))) # display
        sleep(2)
    
    def getPressure(self, sense):
        pressure = sense.get_pressure()
        sense.show_message("Pressure: ")
        sense.show_message(str(round(pressure,2)))

sense = SenseHat() # initializing object
environmentData = EnvironmentData()

# getting/displaying temperature from object
sense.clear()
environmentData.getTemperature(sense)

# getting/displaying humidity
sense.clear()
environmentData.getHumidity(sense)

# getting/displaying pressure
sense.clear()
environmentData.getPressure(sense)


