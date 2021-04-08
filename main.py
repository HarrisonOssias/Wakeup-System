import time
import threading 
#import RPi.GPIO as GPIO
#from actions.alarm import Buzzer
#from actions.slapper import Stepper
from routes.tweets import BlinkyStreamer
from dotenv import dotenv_values #must be using .env file to store twitter API keys
from .routes.tweets import start

config = dotenv_values(".env") #get keys from .env file and store in dictionary  

# Search terms
TERMS = '#HOssias'

# Setup GPIO as output
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, GPIO.LOW)

if __name__ == '__main__':
    try:
        #stream = BlinkyStreamer(config["APP_KEY"], config["APP_SECRET"], config["OAUTH_TOKEN"], config["OAUTH_TOKEN_SECRET"])
        #stream.statuses.filter(track=TERMS)
        start()
    except KeyboardInterrupt:
        GPIO.cleanup()
