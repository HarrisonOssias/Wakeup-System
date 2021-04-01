import RPi.GPIO as GPIO
from threading import Thread
import time


class Stepper:
    def __init__(self):
        self.motorPins = (12, 16, 18, 22)
        self.CCWStep = (0x01, 0x02, 0x04, 0x08)
        self.CWStep = (0x08, 0x04, 0x02, 0x01)
        GPIO.setmode(GPIO.BOARD)
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

class Buzzer:
    def __init__(self):
        self.buzzerPin = 32    # GPIO 12, PWM0
        GPIO.setup(self.buzzerPin, GPIO.OUT) 
        self.pwm = GPIO.PWM(self.buzzerPin, 500) # 500 default freq
    def startBuzzer(self):
        self.pwm.start(50) # 50% duty cycle
    def stopBuzzer(self):
        self.pwm.stop()
    def changeFreq(self, freq):
        self.pwm.ChangeFrequency(freq)
    def play(self, noteList, noteDurationList):
        self.pwm.start(50)
        for index, note in enumerate(noteList):
            self.changeFreq(note)
            time.sleep(noteDurationList[index])

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


def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try: 
        MyStepper = Stepper()
        StepperThread = Thread(target=MyStepper.slap)
        StepperThread.start() #starts
        MyBuzzer = Buzzer()
        BuzzerThread = Thread(target=MyBuzzer.play, args=([500,600,700], [1,1,1],))
        BuzzerThread.start() #starts
        MyPump = Pump()
        MyPump.switchPump()
        time.sleep(5)
        MyPump.switchPump()
        #todo
    except KeyboardInterrupt: 
        destroy()