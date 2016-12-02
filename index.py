'''from TwitterSearch import *
from twitter import *
import urllib

r = urllib.urlopen('https://api.twitter.com/1.1/trends/place.json?id=1').read()
print r








try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'UtvgXDJeHGZoL8naPRBVQJBTU',
        consumer_secret = 'xUO1RzRoIqQBP5pMhiscLBDyRH9cLEUtw8WtgZ9RvFI721MR8I',
        access_token = '2955186811-3knD17GyGB21G1obeECLiMA5NsJTNU1tkeBG94J',
        access_token_secret = '7Ba84Alidfz9nAZWcb33EFW2DmeCyxr9SJoXvVYyEkzDx'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) ).encode('utf-8')

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)



'''

from twitter import *
import urllib
import json

def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        #w = Label(master, text=line1 + "\n" + line2 + "\n\n")
       # print line1.encode('utf-8') + " " + line2.encode('utf-8')
       

def getTweets():

    x = t.statuses.home_timeline(screen_name="kumarnitin917")
    return x


def tweet():

    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")

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


with open('woeid.json') as data_file:
    woeid_list = json.load(data_file)

length = len(woeid_list['array'])


for i in range(0,length):
    try:    
        print str(woeid_list['array'][i]['parentid'])
        r = t.trends.place(_id = woeid_list['array'][i]['parentid']) 
        print r
    except:
        print "error"


#getTrends()