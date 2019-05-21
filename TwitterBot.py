import tweepy 
import urllib
import re
from twython import Twython

class Bot:
    def __init__(self, keys):
        self._consumer_key = keys[0]
        self._consumer_secret = keys[1]
        self._access_token = keys[2]
        self._access_secret = keys[3]

        try:
            auth = tweepy.OAuthHandler(self._consumer_key,
                                       self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)

            self.client = tweepy.API(auth)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print 'There was an error: ',e[0][0]['message'], 'Error code:',e[0][0]['code']
            exit(0)
        else:
            print('Connected as @{}'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id

    def post_tweet(self, img_path, text_to_tweet):
        CONSUMER_KEY = self._consumer_key
        CONSUMER_SECRET = self._consumer_secret
        OAUTH_TOKEN = self._access_token
        OAUTH_TOKEN_SECRET = self._access_secret

        # Twitter API object creation
        twyapi = Twython(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

        try:
            if (img_path=="noPIC"):
                response = twyapi.update_status(status=text_to_tweet)
            else:
                # Uploading image
                image = open(img_path, 'rb')
                media_uploaded = twyapi.upload_media(media=image)
                media_id = media_uploaded['media_id']

                # Posting the tweet
                response = twyapi.update_status(status=text_to_tweet, media_ids=media_id)
        except:
            print "An error occurred while posting the tweet."
            exit(-1)


    def get_tweet_in_position(self, position):

        if position=="lastTweet":
            tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
        else:
            tweet = self.client.user_timeline(id=self.client_id, count=2)[1]
        return tweet.text

    def get_pic_url_of_tweet(self, tweet):

        tweet_urls = re.findall(".*\s(\S*)", tweet)
        tweet_link = tweet_urls[len(tweet_urls) - 1]

        f = urllib.urlopen(tweet_link)
        src_tweet = f.read()

        tweet_pic_urls = re.findall('src=\"(https:\/\/pbs.twimg\S*)\"', src_tweet)
        tweet_pic_url = tweet_pic_urls[len(tweet_pic_urls) - 1]
        return tweet_pic_url





