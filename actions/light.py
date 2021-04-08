import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
class Light:
    def __init__(self):
        self.ledPin = 21 # GPIO 16
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
