import asyncio
from twscrape import API

ACCOUNTS = [
    #accounts here
]

class Scrape:
        
    def __init__(self):
        
        self.api = API()
        
        asyncio.run(self.initializeAccounts())
                
    async def initializeAccounts(self):
        
        for account in ACCOUNTS:
            
            await self.api.pool.add_account(account[0], account[1], account[2], account[3])
    
        await self.api.pool.login_all()
    
    async def searchTweets(self, query: str):
        
        tweets = []
        
        async for tweet in self.api.search(query, limit=45):
    
            tweets.append(tweet.rawContent)
            
        return tweets
