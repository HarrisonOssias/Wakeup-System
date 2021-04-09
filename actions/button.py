import RPi.GPIO as GPIO
import time
from twython import Twython
from dotenv import dotenv_values




class Button:
    def __init__(self):
        self.buttonPin =     # GPIO 
        self.config = dotenv_values(".env")
        self.C_KEY = config["APP_KEY"]
        self.C_SECRET = config["APP_SECRET"]
        self.A_TOKEN = config["OAUTH_TOKEN"]
        self.A_SECRET = config["OAUTH_TOKEN_SECRET"]
        self.api = Twython(self.C_KEY, self.C_SECRET, self.A_TOKEN, self.A_SECRET)
    def listen(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down=GPIO.PUB_UP) 
        while True:
            if GPIO.input(self.buttonPin)==GPIO.LOW:
                api.update_status(status = "I am awake!")
        GPIO.cleanup()