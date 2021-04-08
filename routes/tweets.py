from twython import TwythonStreamer
from threading import Thread
from collections import deque   
from requests.exceptions import ChunkedEncodingError
import time
from dotenv import dotenv_values #must be using .env file to store twitter API keys


# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def __init__(self, consumer_key, consumer_secret, token, token_secret, tqueue):
        self.tweet_queue = tqueue
        super(TwitterStream, self).__init__(consumer_key, consumer_secret, token, token_secret)

    def on_success(self, data):
        if 'text' in data:
            self.tweet_queue.append(data)

    def on_error(self, status_code, data):
        print(status_code)
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

TERMS = "HOSSIAS"               
                
config = dotenv_values(".env") #get keys from .env file and store in dictionary  

def stream_tweets(tweets_queue):

    try:
        stream = BlinkyStreamer(config["APP_KEY"], config["APP_SECRET"], config["OAUTH_TOKEN"], config["OAUTH_TOKEN_SECRET"])

        # You can filter on keywords, or simply draw from the sample stream
        #stream.statuses.filter(track='twitter', language='en')
        stream.statuses.sample(track=TERMS)
    except ChunkedEncodingError:
        # Sometimes the API sends back one byte less than expected which results in an exception in the
        # current version of the requests library
        stream_tweets(tweet_queue)

        
            
def process_tweets(tweets_queue):
    while True:
        if len(tweets_queue) > 0:
            #  Do something with the tweets
            print(tweets_queue.popleft())

if __name__ == '__main__':

    tweet_queue = deque()

    tweet_stream = Thread(target=stream_tweets, args=(tweet_queue,), daemon=True)
    tweet_stream.start()

    process_tweets(tweet_queue)