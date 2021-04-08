import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
class Pump:
    def __init__(self):
        self.pumpPin = 36 # GPIO 16
        self.pumpOn = True
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        if (self.pumpOn = True):
            self.pumpOn = false
        else:
            self.pumpOn = True
        GPIO.output(self.pumpPin, self.pumpOn if GPIO.LOW else GPIO.HIGH)
    def getState(self):
        return self.pumpOn


if __name__ == '__main__':
    pump = Pump()

    pump.switchPump()
    time.sleep(3)
    print(pump.getState())
    pump.switchPump()
    print(pump.getState())    