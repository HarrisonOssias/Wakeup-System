import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
class Pump:
    def __init__(self):
        self.pumpPin = 36 # GPIO 16
        self.pumpOn = True
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        self.pumpOn = self.pumpOn if False else True
        GPIO.output(self.pumpPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.pumpPin, GPIO.LOW)

    def getState(self):
        return self.pumpOn


if __name__ == '__main__':
    pump = Pump()

    pump.switchPump()
    time.sleep(3)
    print(pump.getState())
    pump.switchPump()
    print(pump.getState())    