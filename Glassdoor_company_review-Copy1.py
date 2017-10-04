
# coding: utf-8

# In[95]:

import json
import requests 
import numpy as np
import pandas as pd
from urllib.parse import quote
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from itertools import cycle, islice


# In[143]:

baseUrl = "http://api.glassdoor.com/api/api.htm?format=json&v=1&action=employers&l=USA&returnCities=true"

partnerId = "199084"

partnerKey = "D3Ee1oQ6L9"

query = "Data Analyst"#"SharePoint Architect"

location = "USA"

url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey+"&q="+ quote(query)+"&l="+ quote(location)
headers = {'user-agent': 'Mozilla/5.0'}
maxCount =100
ps =10
pn =1
employerdata =[]
for pn in range(1,int(maxCount/ps)+1):
    pagedUrl = url+ "&ps="+str(ps)+"&pn="+str(pn)
    print(pagedUrl)
    response=requests.get(pagedUrl ,headers=headers).json()
    for x in response["response"]["employers"]:
        employerdata.append({"name":x["name"],
                             "headline": x['featuredReview']["headline"],
                             "pros": x['featuredReview']["pros"],
                             "cons": x['featuredReview']["cons"],
                             "city": x['featuredReview']["location"]}  )
print(len(employerdata))
#employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
#print(len(employerdata_df))
#employerdata_df


# In[144]:

employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
#print(len(employerdata_df))
employerdata_df.head()


# In[146]:

for x in employerdata:
    client = language.LanguageServiceClient()
    document = types.Document(content=x["pros"],type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    x["pros_score"] = sentiment.score
    x["pros_magnitude"] = sentiment.magnitude
    document = types.Document(content=x["cons"],type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    x["cons_score"] = sentiment.score
    x["cons_magnitude"] = sentiment.magnitude

employerdata


# In[147]:

for x in employerdata:
    if(len(x["city"].split(',')) == 2):
        x["state"] =(x["city"].split(',')[1])
    x["combined_r"] = x["pros_score"]*x["pros_magnitude"] + x["cons_score"]*x["cons_magnitude"]
    if x["pros_score"]*x["pros_magnitude"] + x["cons_score"]*x["cons_magnitude"] >  1:
        x["combined_rating"] = 'Good'
    if (x["pros_score"]*x["pros_magnitude"] + x["cons_score"]*x["cons_magnitude"]) < 1:
        x["combined_rating"] = 'Neutral'
    if x["pros_score"]*x["pros_magnitude"] + x["cons_score"]*x["cons_magnitude"] < 0:
        x["combined_rating"]  = 'Poor'


# In[148]:

employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
print(len(employerdata_df))
employerdata_df.head()


# In[154]:

city_df=pd.DataFrame(employerdata_df.groupby("city")["combined_r"].mean())
city_df   
colors = list(islice(cycle(['b', 'g', 'y']), None, len(city_df)))
city_chart = city_df.plot(kind="bar", title=" City wise sentiment analysis for Data Analyst in USA", color=colors,figsize=(15,5))
city_chart.set_xlabel("cities")
city_chart.set_ylabel("Review Score")
plt.show()

#city_df


# In[129]:

employerdata_df["city"].unique()


# In[157]:

state_df=pd.DataFrame(employerdata_df.groupby("state")["combined_r"].mean())
state_df   
colors = list(islice(cycle(['b', 'g', 'y']), None, len(state_df)))
state_chart = state_df.plot(kind="bar", title=" State wise sentiment analysis for Data Analyst in USA", color=colors,figsize=(15,5))
state_chart.set_xlabel("State")
state_chart.set_ylabel("Review Score")
plt.show()
#city_df


# In[158]:

employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
print(len(employerdata_df))
employerdata_df
colors =['LightSkyBlue','green','red','blue','gold']
ratings = employerdata_df["combined_rating"].unique()
for i, rating in enumerate(ratings):
        #print(channel)
        b=employerdata_df[employerdata_df["combined_rating"]==rating]
        b["combined_r"]
        # Plot Time Between Twets
        plt.scatter(range(len(b)),
               b["combined_r"], 
                c=colors[i],
                edgecolors="black",   
                marker="o",
                linewidths=1,
                s=100,
                label= rating,
                alpha=0.8)
        plt.grid(True)
        sns.set()
lgnd = plt.legend() 
plt.title("Scatter plot of Reviews of Employers with Data Analyst job in USA")
plt.xlim([len(b)+5,-2])
plt.xticks(np.arange(len(b),10,10))
plt.yticks(np.arange(-1.0,1.0+0.5,0.5))
plt.show()
#employerdata_df.groupby("combined_rating")["city"].nunique()


# In[57]:

# employerdata_df
# employerdata_df.to_csv("Glassdoor4.csv")


# In[159]:

# employerdata


# In[ ]:

# file = 'Glassdoor4.csv'
# df4 = pd.read_csv(file, encoding='utf-8')
# df4.head()


# In[ ]:

# file = 'glassdoor_review_result.csv'
# comapny_review_df = pd.read_csv(file,encoding='utf-8' )
# comapny_review_df.groupby('name')
# comapny_review_df


# In[ ]:


combined_df=pd.DataFrame(comapny_review_df.groupby(['combined_rating'])['name'].count())

combined_df


# In[160]:

# colors =['green','blue','gold','red'] 
# types = combined_df.name.unique()
# for i, t in enumerate(types):
#         c = combined_df[combined_df['combined_rating']==t]    
#         a= plot.bar( c["combined_rating"],
#                    c['name'],
#                    c=colors[i],
#                    width=1.0,
#                    edgecolor='black',
#                    label=t)
# lgnd = plt.legend() 
# plt.ylabel("Number Of Companies ")
# plt.xlabel("Combined_rating Analysis") 
# plt.title("Companies categaries ") 
# plt.grid(False) 
 
# #plt.legend(loc='upper center', bbox_to_anchor=(1.25, 1),title="company catageries", shadow=True, ncol=1)
# sns.set() 
# plt.savefig("combined_rating.png")
# plt.show()

# for i, t in enumerate(types):
#     c = city_df[city_df['CityType'] == t]
#     a = plt.scatter(c['Totalrides'],
#             c['Avgfare'],
#             s=c["TotalDrivers"]*30,
#             c=colors[i],
#             edgecolor="black",   
#             marker="o",
#             alpha=0.7,
#             facecolor='gray',        
#             linewidths=1,        
#             label=t)
    #handleList.append(a)






# In[ ]:



