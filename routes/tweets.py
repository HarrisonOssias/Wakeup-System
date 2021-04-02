from twython import TwythonStreamer

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        n = 0
        while (n <= 10):
            if 'text' in data:
                print (data['text'] + "Was added to queue") #set tweet
                n++
