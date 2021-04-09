import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self):
        self.buzzerPin = 32    # GPIO 12, PWM0
        self.pwm = GPIO.PWM(self.buzzerPin, 500) # 500 default freq
    def startBuzzer(self):
        self.pwm.start(50) # 50% duty cycle
    def stopBuzzer(self):
        self.pwm.stop()
    def changeFreq(self, freq):
        self.pwm.ChangeFrequency(freq)
    def play(self, noteList, noteDurationList):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buzzerPin, GPIO.OUT) 
        self.pwm.start(50)
        for index, note in enumerate(noteList):
            self.changeFreq(note)
            time.sleep(noteDurationList[index])

        GPIO.cleanup()
