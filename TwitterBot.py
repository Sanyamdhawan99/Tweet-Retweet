import tweepy

# used titter app to get these values
consumer_key = 'enyvfQfcNJStRmKwvtIguuy5A'
consumer_secret = 'PRaQdiwPYHYavP2gWy8UaIFDbSAVKXSJB2wYt46TpkqihRuhiX'
access_token = '900680404536930306-m4eaEHTTtARJ4l1ySAUJcLvJxe1YW4m'
access_token_secret = 'HO2MRrije8VgUMeey0H4TxNgXbpdSb11XAXWm2o4II1ZI'

# authorization using OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# access token
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set up a user --> calling myself
user = api.me()
print(user.name) # will print the name of the user


def main():
    # set up the search criteria
    search = ("coding")
    number_of_tweets = 100
    """
        api.search --> search in the api and returns items number of tweets time
    """
    for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            print('stopped')
            break


main()

