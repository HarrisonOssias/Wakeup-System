import RPi.GPIO as GPIO
import time


class Light:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.ledPin = 35 # GPIO 19
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.pumpPin, GPIO.LOW)
    def turnOn(self):
        GPIO.output(self.pumpPin, GPIO.HIGH)
    def turnOff(self):
        GPIO.output(self.pumpPin, GPIO.LOW)
    def run(self):
        self.turnOn()
        time.sleep(5)
        self.turnOff()
        GPIO.cleanup()
