import json
import os

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

#Filename = str(input("File name: "))
Filename = os.path.dirname(os.path.abspath(__file__))+'\\twitter.json'
Request = int(input("input : "))

Data = read_json(Filename)

class Twitter_database:
    def __init__(self,data) -> None:
        self.data = data
        self.number_tweet ,self.number_user = 0 , 0
        self.most_tweet_user = []
        self.username_data , self.username_num_tweet = [],None
        self.number_topics , self.topics = 0,[]
        self.type_topic_priority , self.topic_priority = None,[]
        self.most_tweet_word = 0

    def get_number_tweet(self):  #+ 1
        self.number_tweet = len(self.data)
        return self.number_tweet
    
    def get_number_user(self):   #+ 2
        username_data = []
        name_topic_priority = []

        for i in range(self.get_number_tweet()):
            username_data.append(self.data[i]['author'])
            name_topic_priority.append(self.data[i]['topic_priority'])

        self.username_data = username_data
        self.topic_priority = list(set(name_topic_priority))

        self.number_user = len(set(username_data))
        return self.number_user
    
    def get_most_tweet_user(self):  #+ 3

        self.username_num_tweet = {name: 0 for name in self.username_data}
        for item in self.data:
            if 'author' in item and item['author'] in self.username_data:
                self.username_num_tweet[item['author']] += 1
        max_tweet = max(self.username_num_tweet.values())
        most_tweet_user = []

        for key,value in self.username_num_tweet.items():
            if value == max_tweet:
                most_tweet_user.append(key)

        return most_tweet_user
    
    def get_number_topic(self):  #+ 4
        for i in range(self.get_number_tweet()):
            self.topics.append(self.data[i]['topic'])
        self.number_topics = len(set(self.topics))
        return self.number_topics
    
    def get_number_topics_by_name(self,Type):   #+ 5,6

        self.num_topic_priority = {name: 0 for name in self.topic_priority}
        for item in self.data:
            try:
                tps = item.get('topic_priority')
                if tps in self.num_topic_priority:
                    self.num_topic_priority[tps] += 1
            except:
                pass

        return self.num_topic_priority.get(Type)   
    
    def check_languages(self):  #+ 7
        lang = []
        for i in range(self.get_number_tweet()):
            lang.append(self.data[i]['language'])
        
        if len(set(lang)) == 1:
            return False
        else:
            return True
    
    def get_most_tweet_word(self):
        most_word = 0
        for i in range(self.get_number_tweet()):
            self.get_most_tweet_word = len(self.data[i]['text'].split())
            if self.get_most_tweet_word > most_word:
                most_word = self.get_most_tweet_word

        self.get_most_tweet_word = most_word
        return self.get_most_tweet_word
            

        
TW = Twitter_database(Data)
TW.get_number_user() #*2

if Request == 1:
    print(TW.get_number_tweet())
elif Request == 2:
    print(TW.get_number_user())
elif Request == 3:
    for i in TW.get_most_tweet_user():
        print(i)
elif Request == 4:
    print(TW.get_number_topic())
elif Request == 5:
    print(TW.get_number_topics_by_name('ALERT'))
elif Request == 6:
    print(TW.get_number_topics_by_name('UNIMPORTANT'))
elif Request == 7:
    print(str(TW.check_languages()))
elif Request == 8:
    print(TW.get_most_tweet_word())
else:
    print('')