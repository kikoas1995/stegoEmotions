import TwitterBot as Bot
import Emotions
import AESciphersuite as AEScs
import argparse


class stegoEmotions(object):
    def __init__(self):
        self.TwitterKeys =
        self.AzureCognitiveSubscription_key = 

    def hide(self):
        bot = Bot.Bot(self.TwitterKeys)

        img_path = raw_input("Introduce the name of the picture to upload: ")
        text_to_tweet = raw_input("Introduce the text of the tweet: ")

        bot.post_tweet(img_path, text_to_tweet)

        tweet = bot.get_tweet_in_position("lastTweet")

        tweet_pic = bot.get_pic_url_of_tweet(tweet)

        emotion = Emotions.Emotions(self.AzureCognitiveSubscription_key)
        pre_key = emotion.getEmotionsSum(tweet_pic)

        print("The value used to genereate the key is %s" % (pre_key))

        AES = AEScs.AESciphersuite(str(pre_key))
        text_to_encrypt = raw_input("Introduce the text you want to encrypt and post: ")

        encrypted_text = AES.encrypt(text_to_encrypt)
        bot.post_tweet("noPIC", encrypted_text)

    def reveal(self):
        bot = Bot.Bot(self.TwitterKeys)

        tweet_to_decrypt = bot.get_tweet_in_position("lastTweet")

        tweet_with_pic = bot.get_tweet_in_position("prelastTweet")
        pic_url = bot.get_pic_url_of_tweet(tweet_with_pic)

        emotion = Emotions.Emotions(self.AzureCognitiveSubscription_key)
        pre_key = emotion.getEmotionsSum(pic_url)
        print("The value used to genereate the key is %s" % (pre_key))

        AES = AEScs.AESciphersuite(str(pre_key))

        tweet_in_clear = AES.decrypt(tweet_to_decrypt)
        print ("-->The text in clear of the last tweet is: ")
        print "    ",tweet_in_clear



def parse_args():
    parser = argparse.ArgumentParser(
        description='stegoEmotions: a steganographic tool to hide and reveal messages in tweets. '
                    'Using CognityServices Face API (running in Azure) to hide messages on Pics uploaded on twitter',
        epilog='if no optionals arguments are passed the default behavior is to hide a message: stegoEmotions --hide')
    parser.add_argument('--hide', action='store_true', required=False, help='To hide a message posting two tweets')
    parser.add_argument('--reveal', action='store_true', required=False, help='To reveal the last message posted by this tool')

    args = parser.parse_args()
    return args


def main():

    args = parse_args()

    stego=stegoEmotions()
    if args.reveal:
        stego.reveal()
    else:
        stego.hide()


if __name__ == "__main__":
    main()