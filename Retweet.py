import tweepy
import time

auth = tweepy.OAuthHandler('yBLmoPy36OOUBGHRzisHv3Hp', 'bxPJsUSI4rsyrAGxXKBzQrAm6lTJY1HQF8zvTE0YSAC9BoqqR')
auth.set_access_token('3647824512-Gw0RPSXa37iEnbHqKUyxjDR2Y9BNCw0TNlKSOe','9lO8Vx2eELk5z9EgAb2Jlob5HaEuCPaLj2tipuqsE965')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'Javascript'
nrTweets = 500
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
