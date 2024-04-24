from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

class TwitterSentiment:
    
    def __init__(self):
        
        self.roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.roberta)
        self.tokenizer = AutoTokenizer.from_pretrained(self.roberta)
        self.labels = ["Negative", "Neutral", "Positive"]
    
    def preprocess(self, tweets: list):
        
        processed = []
        
        for tweet in tweets:
            
            words = []
            
            for word in tweet.split(' '):
                
                if(word.startswith('@') and len(word) > 1):
                    word = '@user'
                elif word.startswith('http'):
                    word = "http"
                    
                words.append(word)
                
            processed.append(" ".join(words))
            
        return processed
                
    def analysis(self, tweets: list):
        
        ptweets = self.preprocess(tweets)
        
        sums = [0, 0, 0]
        
        for tweet in ptweets:
            
            etweet = self.tokenizer(tweet, return_tensors='pt')
            output = self.model(**etweet)
            scores = output[0][0].detach().numpy()
            
            # print(softmax(scores))
            sums[0] += scores[0]
            sums[1] += scores[1]
            sums[2] += scores[2]
            
        sums[0] = sums[0] / len(ptweets)
        sums[1] = sums[1] / len(ptweets)
        sums[2] = sums[2] / len(ptweets)
        sums = softmax(sums)
        
        return sums
