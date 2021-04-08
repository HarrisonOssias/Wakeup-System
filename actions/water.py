import RPi.GPIO as GPIO
import time


class Pump:
    def __init__(self):
        self.pumpPin = 40 # GPIO 21
        self.pumpOn = True
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        self.pumpOn = self.pumpOn if False else True
        GPIO.output(self.pumpPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.pumpPin, GPIO.LOW)

    def getState(self):
        return self.pumpOn