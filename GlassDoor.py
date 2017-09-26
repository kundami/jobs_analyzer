
# coding: utf-8

# In[361]:

import json
import requests 
import numpy as np
import pandas as pd
from urllib.parse import quote


# In[362]:

#url="http://api.glassdoor.com/api/api.htm?t.p=199084&t.k=D3Ee1oQ6L9&userip=10.0.0.133&format=json&v=1&action=jobs-stats&jc=9&l=USA&admLevelRequested=1&returnJobTitles=true&returnCities=true"

baseUrl = "http://api.glassdoor.com/api/api.htm?format=json&v=1&action=jobs-stats&l=USA&returnCities=true"
partnerId = "199084"
partnerKey = "D3Ee1oQ6L9"
query = "Data Analyst"#"SharePoint Architect"
#jobTitle = "Data Analyst"
url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey+"&q="+ quote(query)
#print(url)

#url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey +"&jt="+ quote(jobTitle)
#print(url)


# In[363]:

headers = {'user-agent': 'Mozilla/5.0'}
response=requests.get(url ,headers=headers).json()
#print(json.dumps(response,indent=2))
print(len(response["response"]["cities"]))

citydata = response["response"]['cities']
citydata_df= pd.DataFrame.from_dict(citydata, orient='columns')
citydata_df.head()


# 

# In[383]:


baseUrl = "http://api.glassdoor.com/api/api.htm?format=json&v=1&action=employers&l=USA&returnCities=true"
partnerId = "199084"
partnerKey = "D3Ee1oQ6L9"
query = ""#"SharePoint Architect"
#location = "New York, NY"
url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey+"&q="+ quote(query)+"&l="+ quote(location)
headers = {'user-agent': 'Mozilla/5.0'}
maxCount =100
ps =10
pn =1
employerdata =[]
for pn in range(1,int(maxCount/ps)+1):
    pagedUrl = url+ "&ps="+str(ps)+"&pn="+str(pn)
    #print(pagedUrl)
    response=requests.get(pagedUrl ,headers=headers).json()
    for x in response["response"]["employers"]:
        employerdata.append({"name":x["name"],
                             "headline": x['featuredReview']["headline"],
                             "pros": x['featuredReview']["pros"],
                             "cons": x['featuredReview']["cons"]}  )
#print(len(employerdata))
employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
print(len(employerdata_df))
employerdata_df
#a.duplicated()


# In[384]:




# In[ ]:




# In[ ]:



