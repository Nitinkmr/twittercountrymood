from twitter import *
import urllib
import json

def getTrends(country_id):
    
    try:
        r = t.trends.place(_id = country_id)#urllib.urlopen('https://api.twitter.com/1.1/trends/place.json?id=1').read()
        print r
    except:
        print "error"


# Put in token, token_key, con_secret, con_secret_key

t = Twitter(
    auth=OAuth('2955186811-3knD17GyGB21G1obeECLiMA5NsJTNU1tkeBG94J', 
               '7Ba84Alidfz9nAZWcb33EFW2DmeCyxr9SJoXvVYyEkzDx',
               'UtvgXDJeHGZoL8naPRBVQJBTU',
               'xUO1RzRoIqQBP5pMhiscLBDyRH9cLEUtw8WtgZ9RvFI721MR8I'))

numberOfTweets = 10

#showTweets(getTweets(), numberOfTweets)

trending_tweets = []
with open('woeid.json') as data_file:
    woeid_list = json.load(data_file)

length = len(woeid_list)
print length

with open("trending_tweets.json",mode="r") as tweets_file:
    #feeds = json.load(tweets_file)
    #tweets_file.write(json.dumps([]))
    feeds = json.load(tweets_file)
    for i in range(0,length):
        element = {};
        element['tweets'] = {}
        feeds[0][woeid_list[i]['country_name']] = element

    for i in range(0,length):
            try:    
                print str(woeid_list[i]['country_name'])
                r = t.trends.place(_id = woeid_list[i]['woeid']) 
                print r
                element = {};
                print len(r[0]['trends'])
                print "\n\n\n\n\n"
                for j in range(0,len(r[0]['trends'])):
                    element[str(j)] = r[0]['trends'][j]['name']
                    feeds[0][woeid_list[i]['country_name']]['tweets'][j] = element[str(j)]
                    #r[0]['trends'][j]['name']

            except Exception as e: 
                print str(e)


with open("trending_tweets.json",mode="w") as tweets_file:
    try:
         tweets_file.write(json.dumps(feeds))
    except Exception as e: 
                print str(e)

