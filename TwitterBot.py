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
            print('ERROR : Conexion fallada')
        else:
            print('Conectado como @{}'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id

    def post_tweet_with_pic(self, ruta_img, txt_del_tweet):
        CONSUMER_KEY = self._consumer_key
        CONSUMER_SECRET = self._consumer_secret
        OAUTH_TOKEN = self._access_token
        OAUTH_TOKEN_SECRET = self._access_secret

        # Creamos el objeto de API de twitter
        twyapi = Twython(CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

        #Enviamos el tweet 

        imagen = open(ruta_img, 'rb')
        media_uploaded = twyapi.upload_media(media=imagen)
        media_id = media_uploaded['media_id']

        # Subimos la imagen
        response = twyapi.update_status(status= txt_del_tweet, media_ids=media_uploaded['media_id'])

    def get_last_tweet(self):

        tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
        return tweet.text

    def get_pic_url_of_last_tweet(self, tweet):

        tweet_urls = re.findall(".*\s(\S*)", tweet)
        tweet_link = tweet_urls[len(tweet_urls) - 1]

        f = urllib.urlopen(tweet_link)
        src_tweet = f.read()

        tweet_pic_urls = re.findall('.*src=\"(https:\/\/pbs.twimg\S*)\".*', src_tweet)
        tweet_pic_url = tweet_pic_urls[len(tweet_pic_urls) - 1]
	return tweet_pic_url


keys = ['dS50XnUWaP9hkZ50kQOECosH0', 'Uhaz0nJvHkx0A1Jmn1BPsOUnXB85cGJQDerDjKXa3c1RhJuaEU', '1129797728027009024-rKegP2cSHizSDmPsIUq3XsEDjS1Q7r', 'wcEtIz8acrhSgZOVuMaO3Uv4qqDk4Wbqg1z64FNvxiOC2']
bot = Bot(keys)

ruta_img = raw_input("Introduce el nombre de la imagen a subir: ")
txt_del_tweet = raw_input("Introduce el texto del tweet a subir: " )

bot.post_tweet_with_pic(ruta_img, txt_del_tweet)

tweet = bot.get_last_tweet()

tweet_pic = bot.get_pic_url_of_last_tweet(tweet)




