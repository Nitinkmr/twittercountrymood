from twitter import *
import urllib
import json

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
    for i in range(0,len(woeid_list)):
        
        country = woeid_list[i]['country_name']
        element = {}
        element['country_name'] = {}
        incoming_tweets[0][country] = element
        print country

        for j in range(0,3):#len(topics[0][country]["tweets"])):
            try:
                r =  t.search.tweets(q = str(topics[0][country]["tweets"][str(j)]))
                for x in range(0,10):#len(r['statuses'])):
                    element[str(index)] = str(r['statuses'][index]['text'].encode('utf-8'))
                    #print r['statuses'][x]['text'].encode('utf-8')
                    incoming_tweets[0][country][index] = element[str(index)]
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