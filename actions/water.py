import RPi.GPIO as GPIO
import time


class Pump:
    def __init__(self):
        self.pumpPin = 40 # GPIO 21
        self.pumpOn = True
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        self.pumpOn = self.pumpOn if False else True
        GPIO.output(self.pumpPin, self.pumpOn if GPIO.LOW else GPIO.HIGH)
    def getState(self):
        return self.pumpOn