import asyncio
from twscrape import API

ACCOUNTS = [
    #accounts here
]

class TwScrape:
        
    def __init__(self):
        
        self.api = API()
        
        asyncio.run(self.initializeAccounts())
                
    async def initializeAccounts(self):
        
        for account in ACCOUNTS:
            
            await self.api.pool.add_account(*account)
    
        await self.api.pool.login_all()
    
    async def searchTweets(self, query: str):
        
        tweets = []
        print((300 * len(ACCOUNTS)) / (690 / 15))
        async for tweet in self.api.search(query, limit=((300 * len(ACCOUNTS)) / (690 / 15))):
    
            tweets.append(tweet.rawContent)
            
        return tweets
