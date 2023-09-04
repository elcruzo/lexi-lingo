import tweepy

all keys = open('twitterkeys', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.0AuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_tken, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

#You can follow accounts on Twitter
""" api.create_friendship('symelcruzo') """

#You can post
""" api.update_status("I am currently writing a Twitter Bot in Python") """

#You can update your profile
""" api.update_profile(description="") """

#You can list out all your followers
"""
user = api.get_user("symelcruzo")

for follower in user.followers():
    print(f"{follower.name} follows {user.name}")
    
    # print(user.name)
    # print(user.description)
"""
    
#You can like tweets from your timeline without manually liking them  
"""
tweets_home = api.home_timeline(count=10)

for tweet in tweets_home:
    if tweet.author.name.lower() != "symelcruzo":
        if not tweet.favorited:
            print(f"Liking {tweet.id} ({tweet.author.name})")
            api.create_favorite(tweet.id)
"""

#YOU CAN MASS-LIKE A USER'S POSTS            
"""
user = api.get_user("lexfridman")

tweets_user = api.user_timeline(user_id=user.id)

for tweet in tweets_user:
    if not tweet.favorited:
        api.create_favorite(tweet.id)
"""

#YOU CAN SEARCH FOR TWEETS WITH THE KEYWORD Q
"""
tweets = tweepy.Cursor(api.search, q="brains", lang="en").items(10)

print([tweet.text for tweet in tweets])
"""