import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# GPIO pin number of LED
LED = 21;

# Search terms
TERMS = '#HOssias'

# Twitter application authentication
APP_KEY = 'SHzioFGUQbRDa1dv6p8TOCc0o'
APP_SECRET = 'b2zleUaweaOYhyir8LlayDVMtFAKHqHLHon5HQiiaQIfxLjUoY'
OAUTH_TOKEN = '971487379805655040-kNOqo4d2EUys5uuLCzyLXcdysJoY0rq'
OAUTH_TOKEN_SECRET = 'fu3RpuNU4O1KeOljUfuXCanimWafC49ip2uNOleAkC7Io'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def __init__(self):
        self.tweet = None
    def on_success(self, data):
        if 'text' in data:
            self.tweet = (data['text']) #set tweet
            print(self.tweet)
            
    def check(self, useCase):
        if (self.tweet == useCase):
            for i in range (5):
                GPIO.output(LED, GPIO.HIGH)
                print("LED ON")
                time.sleep(1)
                GPIO.output(LED, GPIO.LOW)



# Setup GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
    stream = BlinkyStreamer(APP_KEY, APP_SECRET,
                            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.check('Wake UP #HOssias')
    stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
    GPIO.cleanup()
