import json
from country_list import *
import re
import csv
import nltk

stopWords = []
features = []

def getAllStopWords():
	
	fp = open("stopwords.txt",mode="r")
	line = fp.readline()
	stopWords.append('AT_USER')
	stopWords.append('URL')
	
	while  line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords

#end


def processTweet(tweet):
	# process the tweets

	#Convert to lower case
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
	return tweet
#end
def replaceTwoOrMore(s):
	#look for 2 or more repetitions of character and replace with the character itself
	pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
	return pattern.sub(r"\1\1", s)
#end 

def getFeatureVector(tweet):
	featureVector = []
	#split tweet into words
	words = tweet.split()
	
	for w in words:
		#replace two or more with two occurrences
		w = replaceTwoOrMore(w)
		
		#strip punctuation
		w = w.strip('\'"?,.')
		#check if the word stats with an alphabet
		val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
		#ignore if it is a stop word
		if(w in stopWords or val is None):
			continue
		else:
			featureVector.append(w.lower())

	return featureVector
#end



#start extract_features
def extract_features(tweet):
	tweet_words = set(tweet)
	features = {}
	for word in featureList:
		features['contains(%s)' % word] = (word in tweet_words)
	return features
#end


stopWords = getAllStopWords()




inpTweets = csv.reader(open('training_data.csv', 'rb'), delimiter=',', quotechar='|')
featureList = []

tweets = []

for row in inpTweets:
	try:
		sentiment = row[0]
		tweet = row[1]
		processedTweet = processTweet(tweet)
		featureVector = getFeatureVector(processedTweet)
		featureList.extend(featureVector)
		tweets.append((featureVector, sentiment));
	except Exception as e: 
			print str(e)   
#end loop

# Remove featureList duplicates
featureList = list(set(featureList))
print featureList
training_set = nltk.classify.util.apply_features(extract_features, tweets)

print "training set ready"



NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

print "classifier"
# Test the classifier

#Output
#======
#positive

with open("obtained_tweets.json",mode="r") as tweets_file:
	tweets = json.load(tweets_file)

index  = 0
sentiment_value = 0
total_tweets = 0
for country in countries:
	sentiment_value = 0
	total_tweets = 0
	for i in range(0,len(tweets[0][country])):
		try:
			#print tweets[0][country][str(index)].encode('utf-8')
			test_tweet = tweets[0][country][str(index)]
			value =  NBClassifier.classify(extract_features(getFeatureVector(test_tweet)))
			if str(value) == "positive":
				sentiment_value = sentiment_value + 1
			index = index+1
			total_tweets = total_tweets + 1
		except Exception as e: 
			print "error"
			print str(e)
	
	if total_tweets != 0:
		positive_value = (sentiment_value*1.00)/total_tweets
		print "valur is" + str(positive_value)
		if positive_value >= 0.6:
			print str(country) + " is happy"
		elif positive_value>=0.35 and positive_value<=0.5 :
			print str(country) + " is neutral"
		else:
			print str(country) + " is unhappy"
	else:
		print "no data could be found for " + str(country)