import time
import pandas as pd

handle_list= ['list of handles you want the timelines of']

twitter_dict={}
counter=0

for name in handle_list:
  try:
    twitter_dict[name]=[]
    twitter_dict[name].append(miner.mine_user_tweets(user=name, max_pages=17))
    counter = counter +1
    if counter%40==0:
      time.sleep(900) #15 minute sleep time
    #if name invalid print name and remove key
  except:
    print(name, 'is invalid or locked')
    twitter_dict.pop(name)
    
all_tweets = pd.concat([pd.DataFrame(twitter_dict[i][0]) for i in twitter_dict])