import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
    def turnOn(self):
        GPIO.output(self.pumpPin, GPIO.HIGH)
    def turnOff(self):
        GPIO.output(self.pumpPin, GPIO.LOW)
    def run(self):
        self.pumpPin = 35 # GPIO 19
        GPIO.setup(self.pumpPin, GPIO.OUT)
        self.turnOn()
        time.sleep(5)
        self.turnOff()
        GPIO.cleanup()
