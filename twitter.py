# import the module
import csv
from time import sleep

import tweepy

# assign the values accordingly
consumer_key = "Hidden"
consumer_secret = "Hidden"
access_token = "Hidden"
access_token_secret = "Hidden"
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the screen_name of the targeted user
screen_name = "Hidden"

# user = api.get_user(screen_name)


client = tweepy.Client(bearer_token='Hidden')

# Replace user ID
id = "1142626865020059655"
nextToken = ''
index = 0
arr = []
while True:
    if index == 0:
        users = client.get_users_followers(id=id, user_fields=['profile_image_url'],max_results = 1000)
        print('Next Token Current At ' + nextToken)
        nextToken = users.meta['next_token']
        
        index = 1
        for user in users.data:
            print(user.username)
            arr.append(user.username)
        if nextToken == '':
            break
    else :
        users = client.get_users_followers(id=id, user_fields=['profile_image_url'],max_results = 1000, pagination_token=nextToken) 
        try:
            nextToken = users.meta['next_token']
        except :
            print('No more nexts')
            for user in users.data:
                print(user.username)
                arr.append(user.username)
            break
            
        print('Next Token Current At ' + nextToken)
        if index > 2:
            
            index = 0

        index += 1
        for user in users.data:
            print(user.username)
            arr.append(user.username)
        if nextToken == '':
            break      
wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
for x in arr : wtr.writerow ([x])
