# LexiLingo

Welocme to this repository containing the script for a Twitter bot built using Python.

## Table Of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Features](#features)
- [License](#license)
- [Authors](#author)
- [License](#license)

## Description
This Twitter bot is a Python script that leverages the Tweepy library to interact with Twitter's API. It allows you to perform various actions on Twitter, including following accounts, posting tweets, updating your profile, interacting with your followers, and more.

## Getting Started
To use this Twitter bot, you need to set up your Twitter API keys and install the necessary dependencies. Follow these steps to get started:

1. Clone the repository to your local machine and navigate to the project directory:

   ```bash
   git clone https://github.com/elcruzo/lexi-lingo.git
   cd lexi-lingo
   ```
   
2. Create a file named `twitterkeys` and add your Twitter API keys in the following format:

   ```bash
   API_KEY
   API_KEY_SECRET
   ACCESS_TOKEN
   ACCESS_TOKEN_SECRET
   ```

3. Install the required Python libraries using pip:

   ```bash
   pip install tweepy
   ```

4. Run the bot script:

   ```bash
   python main.py
   ```

## Features

### 1. Follow Accounts on Twitter
You can use the bot to follow accounts on Twitter by uncommenting and modifying the following line:
```python
# api.create_friendship('username')
```

### 2. Post Tweets
You can post tweets using the bot by uncommenting and modifying the following line:
```python
# api.update_status("Your tweet goes here")
```

### 3. Update Your Profile
You can update your Twitter profile information by uncommenting and modifying the following line:
```python
# api.update_profile(description="Your new profile description")
```

### 4. List Your Followers
You can list out all your followers using the bot. Uncomment and modify the following code:
```python
# user = api.get_user("yourusername")
# for follower in user.followers():
#     print(f"{follower.name} follows {user.name}")
```

### 5. Like Tweets from Your Timeline
You can like tweets from your timeline without manually liking them. Uncomment and modify the following code:
```python
# tweets_home = api.home_timeline(count=10)
# for tweet in tweets_home:
#     if tweet.author.name.lower() != "yourusername":
#         if not tweet.favorited:
#             print(f"Liking {tweet.id} ({tweet.author.name})")
#             api.create_favorite(tweet.id)
```

### 6. Mass-Like a User's Posts
You can mass-like a user's posts using the bot. Uncomment and modify the following code:
```python
# user = api.get_user("username")
# tweets_user = api.user_timeline(user_id=user.id)
# for tweet in tweets_user:
#     if not tweet.favorited:
#         api.create_favorite(tweet.id)
```

### 7. Search for Tweets
You can search for tweets containing a specific keyword using the bot. Uncomment and modify the following code:
```python
# tweets = tweepy.Cursor(api.search, q="keyword", lang="en").items(10)
# print([tweet.text for tweet in tweets])
```

## Author(s)

[ElCruzo](https://github.com/elcruzo/)

## License

This Twitter bot is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using your Twitter bot and feel free to contribute to its development or customize it to suit your needs!

