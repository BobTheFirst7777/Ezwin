import tweepy
import json

auth = tweepy.OAuthHandler("rIRlNfDSqeKSG3S28y1lftbHB",
                           "FO8ljQPJNZfNucfrIqz4SluY1ZvoidezpZYYR6smsGp19Tiv9X")
auth.set_access_token("871671216901427201-8xLxXu1mGnw9hW268mlTHSn0ayvbXD7",
                      "soFJg6EQbCJmJdj014Zbdeo2MxJlhylBTLyF3ejclZZ3m")
api = tweepy.API(auth)

trendsList = list()

output = list()
transcript = list()


trendsDick = api.trends_place(2295414)
for trend in trendsDick[0]["trends"]:
    trendsList.append(trend["name"])


for i in range(0,4):
    output.append(trendsList[i])
    for tweet in api.search(q=trendsList[i],lang="en",count = 5,result_type="mixed"):
        if(not tweet.retweeted):
            output.append("https://twitter.com/twitter/statuses/"+str(tweet.id))
            transcript.append(tweet.text)
        else:
            i-=1
            count+=1

        

#print(output)

#if((transcript[i])[-23:-18] == 'https'):
        #transcript[i] = (transcript[i])[0:-23]

print(transcript)
