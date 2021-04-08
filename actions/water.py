import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
class Pump:
    def __init__(self):
        self.pumpPin = 21 # GPIO 16
        self.pumpOn = False
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        GPIO.output(self.pumpPin, GPIO.HIGH)
        self.pumpOn = True
        print (self.pumpOn)
        time.sleep(3)
        GPIO.output(self.pumpPin, GPIO.LOW)
        self.pumpOn = False
        print (self.pumpOn)
        time.sleep(3)
        GPIO.cleanup()


if __name__ == '__main__':
    pump = Pump()
    pump.switchPump()