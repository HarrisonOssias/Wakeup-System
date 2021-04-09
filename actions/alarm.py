import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self):
        self.buzzerPin = 11    # GPIO 17
    def play(self, rythm):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buzzerPin, GPIO.OUT) 
        for i in rythm:
            GPIO.output(self.buzzerPin,GPIO.HIGH)
            print ("Beep")
            time.sleep(i) # Delay in seconds
            GPIO.output(self.buzzerPin,GPIO.LOW)
            print ("No Beep")
            time.sleep(i)
        GPIO.cleanup()
