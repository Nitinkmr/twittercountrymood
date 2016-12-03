from twitter import *
import urllib
import json
import re
t = Twitter(
    auth=OAuth('2955186811-3knD17GyGB21G1obeECLiMA5NsJTNU1tkeBG94J', 
               '7Ba84Alidfz9nAZWcb33EFW2DmeCyxr9SJoXvVYyEkzDx',
               'UtvgXDJeHGZoL8naPRBVQJBTU',
               'xUO1RzRoIqQBP5pMhiscLBDyRH9cLEUtw8WtgZ9RvFI721MR8I'))


index = 0

with open("trending_tweets.json",mode="r") as file:
    topics = json.load(file)
with open("woeid.json",mode="r") as id_list:
    woeid_list = json.load(id_list)
with open("obtained_tweets.json",mode="r") as coming_tweets:
    incoming_tweets = json.load(coming_tweets)
    for i in range(0,len(woeid_list)-1):
        
        country = woeid_list[i]['country_name']
        print country

        for j in range(0,len(topics[0][country]["tweets"])):
            try:
                r =  t.search.tweets(q = str(topics[0][country]["tweets"][str(j)]),lang="en")
                for x in range(0,len(r['statuses'])/3):
                    element = {}
                    element[str(index)] = str(r['statuses'][x]['text'].encode('utf-8'))
                    tweet = element[str(index)]
                    tweet = tweet.lower()
                    #Convert www.* or https?://* to URL
                    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
                    #Convert @username to AT_USER
                    tweet = re.sub('@[^\s]+','AT_USER',tweet)
                    #Remove additional white spaces
                    tweet = re.sub('[\s]+', ' ', tweet)
                    #Replace #word with word
                    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
                    #trim
                    tweet = tweet.strip('\'"')



                    #print r['statuses'][x]['text'].encode('utf-8')
                    incoming_tweets[0][country][index] = tweet
                    print "added"
                    index = index+1
                  #  print "\n\n"
            except Exception as e: 
                print str(e)
        print "\n"


with open("obtained_tweets.json",mode="w") as tweets_file:
    try:
         tweets_file.write(json.dumps(incoming_tweets))
    except Exception as e: 
                print str(e)

file.close()

id_list.close()


coming_tweets.close()

tweets_file.close()