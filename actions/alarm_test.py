import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.buzzerPin = 36    # GPIO 16, PWM0
        GPIO.setup(self.buzzerPin, GPIO.OUT) 
    def startBuzzer(self):
        GPIO.output(self.buzzerPin, GPIO.HIGH)
    def stopBuzzer(self):
        GPIO.output(self.buzzerPin, GPIO.LOW)
    def play(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buzzerPin, GPIO.OUT) 
        for i in range(6):
            self.startBuzzer()
            time.sleep(0.5)
            self.stopBuzzer()
            time.sleep(0.5)

        GPIO.cleanup()

buz = Buzzer()
buz.play()