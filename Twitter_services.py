# Python script for use Twitter API.
# In this case the code allows to get the tweets stream of the specified hashtags

# Required libraries for use this code
#    - Python Tweepy library http://www.tweepy.org/
#    - Python __future__ library

# You need to create a Twitter application with proper permissions in https://apps.twitter.com/

# The required parameters are:
#    - consumer_key (available from Twitter app)
#    - consumer_secret (available from Twitter app)
#    - access_token (available from Twitter app)
#    - access_token_secret (available from Twitter app)
#    - hashtags to monitorize (to be specified in the stream.filter(track=[]) function)

from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="xxxx"
consumer_secret="xxxx"
access_token="xxxxx"
access_token_secret="xxxxx"

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
           return True
       except:
           pass
    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return

     if __name__ == '__main__':
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=['#RSEEjemplosRRSS',#UsosTwitterEnseñanza", "#RSEMiKlout "])
