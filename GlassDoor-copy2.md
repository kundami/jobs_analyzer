

```python
import json
import requests 
import numpy as np
import pandas as pd
from urllib.parse import quote
```


```python
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
```


```python
headers = {'user-agent': 'Mozilla/5.0'}
response=requests.get(url ,headers=headers).json()
#print(json.dumps(response,indent=2))
print(len(response["response"]["cities"]))

citydata = response["response"]['cities']
citydata_df= pd.DataFrame.from_dict(citydata, orient='columns')
citydata_df.head()
```

    1001
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>numJobs</th>
      <th>stateAbbreviation</th>
      <th>stateName</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1132348</td>
      <td>40.71417</td>
      <td>-74.00639</td>
      <td>New York, NY</td>
      <td>5456</td>
      <td>NY</td>
      <td>New York</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1128808</td>
      <td>41.85000</td>
      <td>-87.65000</td>
      <td>Chicago, IL</td>
      <td>2529</td>
      <td>IL</td>
      <td>Illinois</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1147401</td>
      <td>37.77500</td>
      <td>-122.41833</td>
      <td>San Francisco, CA</td>
      <td>2440</td>
      <td>CA</td>
      <td>California</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1138213</td>
      <td>38.89500</td>
      <td>-77.03667</td>
      <td>Washington, DC</td>
      <td>2186</td>
      <td>DC</td>
      <td>District of Columbia</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1154532</td>
      <td>42.35833</td>
      <td>-71.06028</td>
      <td>Boston, MA</td>
      <td>1864</td>
      <td>MA</td>
      <td>Massachusetts</td>
    </tr>
  </tbody>
</table>
</div>




```python

baseUrl = "http://api.glassdoor.com/api/api.htm?format=json&v=1&action=employers&l=USA&returnCities=true"
partnerId = "199084"
partnerKey = "D3Ee1oQ6L9"
query = "NFL"#"SharePoint Architect"
#location = "New York, NY"
url = baseUrl +"&t.p="+partnerId+"&t.k="+partnerKey+"&q="+ quote(query)+"&l="+ quote(location)

headers = {'user-agent': 'Mozilla/5.0'}
response=requests.get(url ,headers=headers).json()
#print(json.dumps(response,indent=2))
#print(len(response["response"]["cities"]))


```


```python
#print(len(response["response"]["employers"]))
employerdata = [x for x in response["response"]["employers"] if x['exactMatch'] == True]
#employerdata = response["response"]['cities']
#employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
#employerdata_df.head()
#print(json.dumps(employerdata,indent=2))
#print( len(employerdata))
employerdata_df= pd.DataFrame.from_dict(employerdata, orient='columns')
employerdata_df.head()
#response["response"]["employers"]
for e in employerdata:
    print(e['name']+" - "+e['featuredReview']["headline"])
```

    NFL - It was a great job. A lot of hands on experience during the 2014 season.
    


```python

```
