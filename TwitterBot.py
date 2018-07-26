import tweepy

# used titter app to get these values
consumer_key = #enter key
consumer_secret = #enter secret
access_token = #enter access token
access_token_secret = #enter access token secret

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
    search = ("coding")  # enter any keyword
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

