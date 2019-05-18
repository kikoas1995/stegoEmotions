import TwitterBot as Bot
import Emotions
import sys

def main(argv):
    
    #Twitterkeys = 
    #AzureCognitiveSubscription_key = 
    ruta_img = input("Introduce el nombre de la imagen a subir: ")
    txt_del_tweet = input("Introduce el texto del tweet a subir: " )    
    
    bot = Bot.Bot(Twitterkeys)
    
    bot.post_tweet_with_pic(ruta_img, txt_del_tweet)

    tweet = bot.get_last_tweet()

    tweet_pic = bot.get_pic_url_of_last_tweet(tweet)
   
    
    emotion = Emotions.Emotions(AzureCognitiveSubscription_key)
    Key = emotion.getEmotionsSum(tweet_pic)
    
    print("The encryption Key is %s" % (Key))

if __name__ == "__main__":
    main(sys.argv[1:])