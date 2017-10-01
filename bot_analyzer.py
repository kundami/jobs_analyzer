# Dependencies
from urllib.parse import quote
#import gmplot
import requests  
import time
import re
import csv
import tweepy
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import cycle, islice
import os
import string
import datetime
import seaborn as sns
sns.axes_style('darkgrid')
sns.set_style('darkgrid')

# Twitter API Keys
consumer_key = "EbkSooRYMpv57pNP4egHICyLm"
consumer_secret = "9KGxBwnwU1fRmfvsivg9yOfQdfXG9yObmZ5rkZXJs7xljmzFS0"
access_token = "912431596619407363-TvMjccUyrG44LErxRNTiB9eyuGFCPNG"
access_token_secret = "IExFYtmvWdXXgFZJiqAZzRssvU1egV9zMLQpGaW6poSQ6"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def analyze_jobs(job_title, request_user):
   
    #url="http://api.glassdoor.com/api/api.htm?t.p=199084&t.k=D3Ee1oQ6L9&userip=10.0.0.133&format=json&v=1&action=jobs-stats&jc=9&l=USA&admLevelRequested=1&returnJobTitles=true&returnCities=true"
    baseUrl = "http://api.glassdoor.com/api/api.htm?format=json&v=1&action=jobs-stats&l=USA&returnCities=true"
    partnerId = "199084"
    partnerKey = "D3Ee1oQ6L9"
    url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey +"&jt="+ quote(job_title)
    print(url)
    
    headers = {'user-agent': 'Mozilla/5.0'}
    response=requests.get(url ,headers=headers).json()
    #print(json.dumps(response,indent=2))
    print(len(response["response"]["cities"]))

    citydata = response["response"]['cities']
    citydata_df= pd.DataFrame.from_dict(citydata, orient='columns')
   
    lats=citydata_df['latitude']
    lons=citydata_df['longitude']
    
    state_name = citydata_df.groupby(['stateName'])
    num_jobs = state_name['numJobs'].sum()
    colors = list(islice(cycle(['b', 'g', 'y']), None, len(citydata_df)))
    job_chart = num_jobs.plot(kind="bar", title=job_title + " Jobs per State in USA", color=colors)
    job_chart.set_xlabel("States")
    job_chart.set_ylabel("Number of jobs")

    #plt.show()
    #--------------------------------
    #plot map image
    x_coords = citydata_df['latitude']
    y_coords = citydata_df['longitude']
    numJobs = citydata_df['numJobs']
    city_name = citydata_df['name']

    df = pd.DataFrame({"Latitude": x_coords,
                        "Longitude": y_coords,
                        "Number of Jobs": numJobs,
                         "City Name": city_name})
    
    import plotly
    import plotly.plotly as py 
    import plotly.graph_objs as go
    #API_Key
    py.sign_in('DemoAccount', '2qdyfjyr7o')
    
    for col in df.columns:
        df[col] = df[col].astype(str)

    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],[0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

    data = [ dict(
            type= 'scattergeo',
            lon = df["Longitude"],
            lat = df["Latitude"],
            locationmode = 'USA-states',
            marker = dict(
                line = dict (
                    color = 'rgb(5,5,5)',
                    width = 2
               ) )        
            ) ]

    layout = dict(
                  title = job_title +' Jobs Statistics per City',
                  geo = dict(
                            scope='usa',
                            projection=dict( type='albers usa' ),
                            showlakes = True,
                            showland = True,
                            lakecolor = 'rgb(255, 255, 255)'),
                            )
    
    fig = dict( data=data, layout=layout )
    py.image.save_as(fig, filename='job-plot.png')
    # time.sleep(120)
    #os.system('cp /c/Users/jingp/Downloads/job-plot.png /c/Users/jingp/OneDrive\Documents\python-challenge\jobs_analyzer/job_analysis/')

    #-----------------------------------------
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'job_analysis/')
    file_name = "tweetout_" + job_title +".png"
    
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.savefig(results_dir + file_name)
    img1=results_dir + file_name
    img2='job-plot.png'
    img3='job_tweet.png'
    dt = datetime.datetime.now().strftime('%m/%d/%Y')
    filenames = [img2, img1,img3]
    media_ids = []
    for filename in filenames:
        res = api.media_upload(filename)
        media_ids.append(res['media_id'])
    print(media_ids)              

    # tweet with multiple images
    api.update_status(status='Job Analysis for'+ job_title + " (" + dt + ") (Thx @" + request_user + "!!!)", media_ids=media_ids)



while(True):
#counter=0
#while (counter==0):
    #Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    df=pd.read_csv('tweet_ids.csv')
    tweet_list=df.values.flatten().tolist()    
    print(tweet_list)
    # Target Search Term
    target_terms = ("@BotAnalyzer job for:")
    # Variable for holding the oldest tweet
    received_tweets = api.search(target_terms, count=100, result_type="recent")
    #print(received_tweets)
    for tweet in received_tweets["statuses"]:
        print(tweet["text"])
        if tweet["id"] not in tweet_list:
            tweet_list.append(tweet["id"]) 
            tweet_text=tweet["text"]
            #print(tweet["text"])
            tweet_text1=re.split(':', tweet_text)
            print(tweet_text1)
            try:
                print(tweet_text1[1])
                job_title=tweet_text1[1]
            except:                             
                job_titl=" "
                print ("Err happened")
                continue                       
            request_user=tweet["user"]["screen_name"]
            print(request_user)
            print(job_title)
            analyze_jobs(job_title, request_user)                       
            my_df = pd.DataFrame(tweet_list)
            print(my_df)
            my_df.to_csv('tweet_ids.csv', sep='\t', encoding='utf-8', index=False)
            
    #print(tweet_list)    
    # Once tweeted, wait 180 seconds before doing anything else
    time.sleep(180)
    #counter +=1

