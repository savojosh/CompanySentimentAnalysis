import os
import asyncio
from TwScrape import TwScrape
from TwitterSentiment import TwitterSentiment

s = TwScrape()
t = TwitterSentiment()
query = "Google (new OR update OR stock OR product) min_replies:50 min_faves:1000"

tweets = asyncio.run(s.searchTweets(query))

print(t.analysis(tweets))

os.remove("accounts.db")
