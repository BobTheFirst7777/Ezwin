import tweepy
import json
from selenium import webdriver 
from time import sleep 
from PIL import Image 


#twitter algorithm

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


trendsDick = api.trends_place(2295414)
for trend in trendsDick[0]["trends"]:
    trendsList.append(trend["name"])


for i in range(0,4):
    output.append(trendsList[i])
    trendsFilter = trendsList[i]+' -filter:retweets'
    for tweet in api.search(q=trendsFilter,lang="en",count = 5,result_type="mixed"):
            output.append("https://twitter.com/twitter/statuses/"+str(tweet.id))
            transcript.append(tweet.text)
            
for i in range(0,len(transcript)-1): 
    if((transcript[i])[-23:-18] == 'https'):
        transcript[i] = (transcript[i])[0:-23]

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


                

