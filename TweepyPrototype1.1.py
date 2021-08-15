import tweepy
import json
from selenium import webdriver 
from time import sleep 
from PIL import Image

from gtts import gTTS
from gtts.tokenizer import pre_processors, Tokenizer, tokenizer_cases
from gtts.utils import _minimize, _len, _clean_tokens, _translate_url
from gtts.lang import tts_langs, _fallback_deprecated_lang
#import os


#twitter algorithm
auth = tweepy.OAuthHandler("rIRlNfDSqeKSG3S28y1lftbHB",
                           "FO8ljQPJNZfNucfrIqz4SluY1ZvoidezpZYYR6smsGp19Tiv9X")#API public and secret keys
auth.set_access_token("871671216901427201-8xLxXu1mGnw9hW268mlTHSn0ayvbXD7",
                      "soFJg6EQbCJmJdj014Zbdeo2MxJlhylBTLyF3ejclZZ3m")#Access token and secret
api = tweepy.API(auth)

trendsList = list()
trendsFilter = str()

output = list()
transcript = list()

countConst = 5

language = 'en'#Language that tts reads
localizer ='ie'#co.uk,ca,co.in,ei,ca

trendsDick = api.trends_place(2295414)#Get list of dictionaries of trends of yahoo WOEID code
for trend in trendsDick[0]["trends"]:
    trendsList.append(trend["name"]) #Make list of lookup terms


for i in range(0,4):
    output.append(trendsList[i])#Name of trend added to list before respective trends
    trendsFilter = trendsList[i]+' -filter:retweets'#Filtering out retweets
    for tweet in api.search(q=trendsFilter,lang="en",count = 5,result_type="mixed",tweet_mode = "extended"):#Tweet lookup
            output.append("https://twitter.com/twitter/statuses/"+str(tweet.id))#Create link for screenshots
            transcript.append(tweet.full_text)#Create transcript for tts
            
for i in range(0,len(transcript)): 
    if((transcript[i])[-23:-18] == 'https'):#Find tweet transcripts with link attached at end
        transcript[i] = (transcript[i])[0:-23]#Remove link

#TTS

for i in range(0,len(transcript)):
    #gtts.tokenizer.pre_processors.abbreviations(transcript[i])
    myobj = gTTS(text=transcript[i],
                 lang=language,
                 tld = localizer,
                 slow=False)
                 #Slow = False to force high speed
    myobj.save(str(i)+"audio.mp3")

#screenshot algorithm

l1=list()
l2=list()
l3=list()
l4=list()
l5=list()
temp=0


for i in range(0,len(output)):
    if (len(output[i])!=56):
        l5.append(output[i])
        temp+=1
    else:
        if temp==1 :
            l1.append(output[i])
        elif temp==2 :
            l2.append(output[i])
        elif temp==3 :
            l3.append(output[i])
        elif temp==4 :
            l4.append(output[i])



driver = webdriver.Chrome("chromedriver.exe")
for a in range(0,len(l1)):
        driver.get(l1[a])
        sleep(2)
        driver.save_screenshot("data/"+str(1)+str(a+1)+".png")
for b in range(0,len(l2)):
        driver.get(l1[b])
        sleep(2)
        driver.save_screenshot("data/"+str(2)+str(b+1)+".png")
for c in range(0,len(l3)):
        driver.get(l3[c])
        sleep(2)
        driver.save_screenshot("data/"+str(3)+str(c+1)+".png")
for d in range(0,len(l4)):
        driver.get(l4[d])
        sleep(2)
        driver.save_screenshot("data/"+str(4)+str(d+1)+".png")

driver.quit()

#cropping algorithm

width = 910
height = 512

for j in range(1,5):
    for k in range(1,6):
        im=Image.open("data/"+str(j)+str(k)+".png")
        im=im.crop((0,0,width,height))
        im=im.resize((1280,720), Image.BOX)
        im.save("data/"+str(j)+str(k)+".png")


                

