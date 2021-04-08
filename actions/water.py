import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
class Pump:
    def __init__(self):
        self.pumpPin = 40 # GPIO 16
        self.pumpOn = False
        GPIO.setup(self.pumpPin, GPIO.OUT)
    def switchPump(self):
        if (self.pumpOn == True):
            self.pumpOn = False
        else:
            self.pumpOn = True
        GPIO.output(self.pumpPin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.pumpPin, GPIO.LOW)


if __name__ == '__main__':
    pump = Pump()

    pump.switchPump()
    time.sleep(3)
    print(pump.getState())
 