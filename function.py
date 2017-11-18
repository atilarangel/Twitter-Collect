import re
from operator import itemgetter
def removeStopWords(y):
    wordList = re.sub(r'[^\w]', " ", y).split()
    stopWords = open('stopwords_portugues.txt', 'r')
    stopWords = stopWords.read()
    new_list = []
    for a in wordList:
        if a not in stopWords:
            new_list.append(a)
    new_list = ' '.join(new_list)
    return new_list

def frequency(user):
    file = open('all_tweets/'+user+'.txt', 'r')
    myDict = {}
    text = []
    for wordList in file:
        wordList = re.sub(r'[^\w]', " ", wordList).split()
        for word in wordList:
            text.append(word)
        for a in text:
            myDict[a] = text.count(a)
    myDict = sorted(myDict.items(), key=itemgetter(1), reverse=1)
    top = myDict[:10]
    n = 0
    while n < len(top):
        for a in top:
            n += 1
            print str(n)+'.', a[0]
            print (str(a[1])).rjust(30)

#user public tweets
def user_tweets(user, public_tweets, stop_w, file):
    if stop_w == 'sim':
        for tweet in public_tweets:
            tt = ((tweet.text).encode('utf-8')).lower()
            removeStop = removeStopWords(tt)
            file.write(removeStop + '\n')
        file.close
    else:
        for tweet in public_tweets:
            file.write(((tweet.text).encode('utf-8')) + '\n')
        file.close


#main function
def anal_tweets(api, user, stop_w, followings, public_tweets, user_followings_list):
    if followings == 'sim':
        if stop_w == 'sim':
            file_followings_list = open('followings_list/' + user + '_followings.txt', 'w')
            file = open('all_tweets/' + user + '.txt', 'w')
            for tweet in public_tweets:
                tt = ((tweet.text).encode('utf-8')).lower()
                removeStop = removeStopWords(tt)
                file.write(removeStop + '\n')
            for followings in user_followings_list:
                public_tweets = api.user_timeline(followings, count=10)
                file_followings_list.write(str(followings)+'\n')
                for tweet in public_tweets:
                    tt = ((tweet.text).encode('utf-8')).lower()
                    removeStop = removeStopWords(tt)
                    file.write(removeStop + '\n')
            file.close
            file_followings_list.close
        else:
            file_followings_list = open('followings_list/' + user + '_followings.txt', 'w')
            file = open('all_tweets/' + user + '.txt', 'w')
            for tweet in public_tweets:
                file.write(((tweet.text).encode('utf-8')) + '\n').lower()
            for followings in user_followings_list:
                public_tweets = api.user_timeline(id=followings, count=10)
                file_followings_list.write(str(followings)+'\n')
                for tweet in public_tweets:
                    file.write(((tweet.text).encode('utf-8')) + '\n')
            file.close
            file_followings_list.close
    else:
        file = open('all_tweets/' + user + '.txt', 'w')
        user_tweets(user, public_tweets, stop_w, file)