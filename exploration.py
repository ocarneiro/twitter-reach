#! /usr/bin/env python3
# coding: utf-8

from secret_tweepy import consumer_key, consumer_secret, \
                          access_token, token_secret
import tweepy
from pprint import pprint


TWEET_TO_ANALYZE = 693201831216943104

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)

tweet = api.get_status(TWEET_TO_ANALYZE)
retweets = api.retweets(TWEET_TO_ANALYZE, 100)

retweeters = {}
for retweet in retweets:
    retweeters[retweet.user.screen_name] = retweet.user.followers_count

print('---------------------------------')
print(tweet.text)
print('---------------------------------')

print('Retweets count: %d' % len(retweets))

print('Tweet reach: %d' % sum(retweeters.values()))

most_influence = sorted(retweeters.items(),
                        key=lambda rt: rt[1],
                        reverse=True)

print('\nMost influencing retweeters:')

pprint(most_influence)
