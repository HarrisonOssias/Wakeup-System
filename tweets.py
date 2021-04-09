from twython import TwythonStreamer
from threading import Thread
from collections import deque
from requests.exceptions import ChunkedEncodingError
import RPi.GPIO as GPIO
import time
# must be using .env file to store twitter API keys
from dotenv import dotenv_values
from actions.alarm import *
from actions.slapper import *
from actions.light import *

GPIO.setwarnings(False)
# Setup callbacks from Twython Streamer


class TwitterStream(TwythonStreamer):
    def __init__(self, consumer_key, consumer_secret, token, token_secret, tqueue):
        self.tweet_queue = tqueue
        super(TwitterStream, self).__init__(
            consumer_key, consumer_secret, token, token_secret)

    def on_success(self, data):
        if 'text' in data:
            self.tweet_queue.append(data['text'])

    def on_error(self, status_code, data):
        print(status_code)
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


# get keys from .env file and store in dictionary
config = dotenv_values(".env")


def stream_tweets(tweets_queue):

    try:
        stream = TwitterStream(config["APP_KEY"], config["APP_SECRET"],
                               config["OAUTH_TOKEN"], config["OAUTH_TOKEN_SECRET"], tweets_queue)
        #stream = BlinkyStreamer(config["APP_KEY"], config["APP_SECRET"], config["OAUTH_TOKEN"], config["OAUTH_TOKEN_SECRET"])

        # You can filter on keywords, or simply draw from the sample stream
        stream.statuses.filter(
            track="@HarrisonOssias,#SLAP323,#WATER323,#ALARM323")

    except ChunkedEncodingError:
        # Sometimes the API sends back one byte less than expected which results in an exception in the
        # current version of the requests library
        stream_tweets(tweet_queue)

    time.sleep(0.5)


def process_tweets(tweets_queue):
    #initialize slapping
    MyStepper = Stepper()
    StepperThread = Thread(target=MyStepper.slap)

    #initialize alarm
    MyBuzzer = Buzzer()
    BuzzerThread = Thread(target=MyBuzzer.play, args=(
    [500, 600, 700], [1, 1, 1],))

    #initialize pump
    MyLED = Light()
    LEDThread = Thread(target=MyLED.run)
    
    while True:
        GPIO.setmode(GPIO.BOARD)
        if len(tweets_queue) > 0:
            #  Do something with the tweets
            action = tweets_queue.popleft()
            print(action)

            if "SLAP323" in action:

                StepperThread.start()

            elif "ALARM323" in action:

                BuzzerThread.start()

            elif "WATER323" in action:
                LEDThread.start()

class Start_tweets():

    def __init__(self):
        self.tweet_queue = deque()
        tweet_stream = Thread(target=stream_tweets, args=(
            self.tweet_queue,), daemon=True)
        tweet_stream.start()
        tweet_process = Thread(target=process_tweets, args=(self.tweet_queue,))
        tweet_process.start()
