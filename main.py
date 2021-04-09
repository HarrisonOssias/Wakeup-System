import time
import threading 
#import RPi.GPIO as GPIO
#from actions.alarm import Buzzer
#from actions.slapper import Stepper
#from routes.tweets import BlinkyStreamer
from dotenv import dotenv_values #must be using .env file to store twitter API keys
from tweets import *



if __name__ == '__main__':
    try:
        #stream = BlinkyStreamer(config["APP_KEY"], config["APP_SECRET"], config["OAUTH_TOKEN"], config["OAUTH_TOKEN_SECRET"])
        #stream.statuses.filter(track=TERMS)
        Start_tweets()
    except KeyboardInterrupt:
        GPIO.cleanup()

