import tweepy
import json

from gtts import gTTS
from gtts.tokenizer import pre_processors, Tokenizer, tokenizer_cases
from gtts.utils import _minimize, _len, _clean_tokens, _translate_url
from gtts.lang import tts_langs, _fallback_deprecated_lang


auth = tweepy.OAuthHandler("rIRlNfDSqeKSG3S28y1lftbHB",
                           "FO8ljQPJNZfNucfrIqz4SluY1ZvoidezpZYYR6smsGp19Tiv9X")
auth.set_access_token("871671216901427201-8xLxXu1mGnw9hW268mlTHSn0ayvbXD7",
                      "soFJg6EQbCJmJdj014Zbdeo2MxJlhylBTLyF3ejclZZ3m")
api = tweepy.API(auth)

trendsList = list()
trendsFilter = str()

output = list()
transcript = list()

countConst = 5

language = 'en-uk'#Language that tts reads
localizer ='ie'#co.uk,ca,co.in,ei,ca


trendsDick = api.trends_place(2295414)
for trend in trendsDick[0]["trends"]:
    trendsList.append(trend["name"])


for i in range(0,4):
    output.append(trendsList[i])
    trendsFilter = trendsList[i]+' -filter:retweets'
    for tweet in api.search(q=trendsFilter,lang="en",count = 5,result_type="mixed",tweet_mode = "extended"):
            output.append("https://twitter.com/twitter/statuses/"+str(tweet.id))
            transcript.append(tweet.full_text)
        

#print(output)
for i in range(0,len(transcript)): 
    if((transcript[i])[-23:-18] == 'https'):
        transcript[i] = (transcript[i])[0:-23]

print(transcript)
print(len(transcript))

for i in range(0,len(transcript)):
    #gtts.tokenizer.pre_processors.abbreviations(transcript[i])
    myobj = gTTS(text=transcript[i],
                 lang=language,
                 tld = localizer,
                 slow=False)
                 #Slow = False to force high speed
    myobj.save(str(i)+"audio.mp3")


