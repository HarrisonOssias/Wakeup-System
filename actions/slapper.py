import RPi.GPIO as GPIO
import time


class Stepper:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.motorPins = (12, 16, 18, 22)
        self.CCWStep = (0x01, 0x02, 0x04, 0x08)
        self.CWStep = (0x08, 0x04, 0x02, 0x01)
        for pin in self.motorPins:
            GPIO.setup(pin, GPIO.OUT)
    def moveOnePeriod(self, direction, ms):
        for j in range(0, 4, 1):
            for i in range(0, 4, 1):
                if (direction == 1):
                    GPIO.output(self.motorPins[i], ((self.CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
                else:
                    GPIO.output(self.motorPins[i], ((self.CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            if(ms<3):
                ms = 3
            time.sleep(ms*0.001)

    def moveSteps(self, direction, ms, step):
        for i in range(step):
            self.moveOnePeriod(direction, ms)

    def motorStop(self):
        for i in range(0, 4, 1):
            GPIO.output(self.motorPins[i],GPIO.LOW)

    def slap(self):
        for i in range(0, 3, 1):
            self.moveSteps(1,3,128) #512 = 360deg, 1=cw, 0=ccw
            time.sleep(0.5)
            self.moveSteps(0,3,128)
            time.sleep(0.5)
        self.motorStop()
        GPIO.cleanup()

