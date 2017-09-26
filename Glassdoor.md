

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
      <td>5270</td>
      <td>NY</td>
      <td>New York</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1147401</td>
      <td>37.77500</td>
      <td>-122.41833</td>
      <td>San Francisco, CA</td>
      <td>2459</td>
      <td>CA</td>
      <td>California</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1128808</td>
      <td>41.85000</td>
      <td>-87.65000</td>
      <td>Chicago, IL</td>
      <td>2459</td>
      <td>IL</td>
      <td>Illinois</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1138213</td>
      <td>38.89500</td>
      <td>-77.03667</td>
      <td>Washington, DC</td>
      <td>2135</td>
      <td>DC</td>
      <td>District of Columbia</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1150505</td>
      <td>47.60639</td>
      <td>-122.33083</td>
      <td>Seattle, WA</td>
      <td>1867</td>
      <td>WA</td>
      <td>Washington</td>
    </tr>
  </tbody>
</table>
</div>






```python

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
```

    100
    




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
      <th>cons</th>
      <th>headline</th>
      <th>name</th>
      <th>pros</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Very large company which can be felt in the of...</td>
      <td>Software Engineer Intern</td>
      <td>IBM</td>
      <td>IBM rented out most of a wework office which a...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Point system isn't enough,  every year or so t...</td>
      <td>Personal/Business Banker</td>
      <td>J.P. Morgan</td>
      <td>Good networking, training in different locatio...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>constant mergers, long hours, construction in ...</td>
      <td>Great company but get ready to work long hours!</td>
      <td>Citi</td>
      <td>Great people, work balance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>long hours\r\nstanding for hours at a time (th...</td>
      <td>Fun place to work</td>
      <td>Macy's</td>
      <td>Fun environment\r\nyou meet a lot of people fr...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Some of the work are not that interesting</td>
      <td>Good Place to Start the Career</td>
      <td>Morgan Stanley</td>
      <td>Many opportunities and most people are friendly</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Can be intense at times and expect a lot from ...</td>
      <td>Very good firm</td>
      <td>Goldman Sachs</td>
      <td>Great people, very good culture. Great reputat...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Work life balance can be hard for all levels e...</td>
      <td>Senior Associate</td>
      <td>PwC</td>
      <td>Many opportunities and diverse environment.</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Intense lifestyle, travel, long hours,  rigid ...</td>
      <td>Consultant</td>
      <td>Deloitte</td>
      <td>Great firm,  mentorship culture,  great benefi...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Sometimes work was a bit dry</td>
      <td>Great place to learn and grow</td>
      <td>EY</td>
      <td>Great company culture and people</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Too much meetings.  Long hours, flexible work ...</td>
      <td>UX</td>
      <td>Bloomberg L.P.</td>
      <td>Nice office environment .  Career sites listin...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Worked mostly alone, didn't have too much inte...</td>
      <td>Software Engineer Intern Review</td>
      <td>Bank of America</td>
      <td>Relaxed work environment, interesting projects...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Very slow growth rate, its better you come out...</td>
      <td>Good company but try to build business</td>
      <td>Cognizant Technology Solutions</td>
      <td>Good in start pay package</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Outdated proprietary technology, slow decision...</td>
      <td>Values Work/Life Balance</td>
      <td>American Express</td>
      <td>Great work/life balance, ability to work in-of...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>None that I can think of.</td>
      <td>Good Sales Environment</td>
      <td>Verizon</td>
      <td>You earn what you put in\r\nflexible hours\r\n...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>None that I can think of.</td>
      <td>Graduate Researcher</td>
      <td>Columbia University</td>
      <td>Quality education. \r\nExemplary faculty.\r\nH...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Yearly raises and base pay are not competitive...</td>
      <td>Good Benefits But Base Pay Too Low</td>
      <td>AIG</td>
      <td>401k and short term incentives are high</td>
    </tr>
    <tr>
      <th>16</th>
      <td>office is out of date</td>
      <td>great experience</td>
      <td>KPMG</td>
      <td>people are awesome and hardworking, collaborative</td>
    </tr>
    <tr>
      <th>17</th>
      <td>-Can be hard applying to other jobs while bein...</td>
      <td>NYU Student Worker is a Solid Position</td>
      <td>NYU (New York University)</td>
      <td>Take my words with a grain of salt since I am ...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Too many layoffs, not enough communication</td>
      <td>Director</td>
      <td>Thomson Reuters</td>
      <td>Great company to work for.  Global experience.</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Purchasing supplies, Cliques, tough administra...</td>
      <td>Secretary</td>
      <td>New York City Department of Education</td>
      <td>Great benefits, dedicated staff, summers and h...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Had to do stuff on my own without any other in...</td>
      <td>Great internship with a lot of experience</td>
      <td>Johnson &amp; Johnson</td>
      <td>Great experience \r\nDid work in all 3 sectors...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Can involve long hours but I assume this would...</td>
      <td>great place to work</td>
      <td>UBS</td>
      <td>very collaborative environment, well compensated</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Bureaucracy like any other firms. Less room fo...</td>
      <td>AVP</td>
      <td>Credit Suisse</td>
      <td>Decent Pay and Good Benefits. Overall, work cu...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Every thing was fine. No cons.</td>
      <td>Its nice working with Barclays. Lots of learni...</td>
      <td>Barclays</td>
      <td>Lots of learning, Competitive salary. Cool wor...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Hard to get promoted . Backroom is kinda heavy...</td>
      <td>Backroom trainer</td>
      <td>Target</td>
      <td>A fun friendly environment . Get to meet new p...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Commutation from Newark Penn station is bad.</td>
      <td>Proctor</td>
      <td>Rutgers University</td>
      <td>It's a nice campus to work.</td>
    </tr>
    <tr>
      <th>26</th>
      <td>layoffs happen yearly, constant changes</td>
      <td>Service Manager</td>
      <td>AT&amp;T</td>
      <td>great benefits, work from home, team-environment</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Other Managers have no idea of what they are d...</td>
      <td>Department Supervisor</td>
      <td>The Home Depot</td>
      <td>Great people in the store to work with. Most M...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Steep learning curve with the number of report...</td>
      <td>Account Analyst</td>
      <td>BNY Mellon</td>
      <td>Great team environment and friendly people. It...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>The hours were bad because they were so early.</td>
      <td>Barista</td>
      <td>Starbucks</td>
      <td>Starbucks was actually a phenomenal place to w...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Globalization has changed work approach. Outso...</td>
      <td>Great Place, Great People. But, changes contin...</td>
      <td>Estée Lauder Companies</td>
      <td>Company provides good benefits and flexible wo...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>I just started working here but it seems like ...</td>
      <td>GAP is an amazing company to work at</td>
      <td>Gap</td>
      <td>Amazing people \nGreat hours \nRoom to grow\nS...</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Poor floor customer service</td>
      <td>Sears cashier</td>
      <td>Sears</td>
      <td>Flexible hours \r\nGood pay plus commission on...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Short term contracts for consultants\nLack of ...</td>
      <td>Expert, Panel if Experts North Korea</td>
      <td>United Nations</td>
      <td>Challenges and opportunities to gain experienc...</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Some technology is a little older</td>
      <td>Digital Producer</td>
      <td>Victoria's Secret Stores</td>
      <td>Great supportive team\r\nFast pace and innovat...</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Difficult and time consuming to get changes im...</td>
      <td>Good people, very bureaucratic</td>
      <td>Wells Fargo</td>
      <td>Quality people with a collaborative attitude\r...</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Your career will be entirely manager/departmen...</td>
      <td>All over the place</td>
      <td>BlackRock</td>
      <td>This is a bigger organization than you'd think...</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Advancement opportunities limited on East Coas...</td>
      <td>Best Engineering Team I have ever worked with</td>
      <td>T-Mobile</td>
      <td>Cutting Edge technology, Fast Paced, highly sk...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>There is not a lot of levels of management so ...</td>
      <td>Great place to work</td>
      <td>Century 21 Department Stores</td>
      <td>The company is growing and has so much opportu...</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Morning shifts are a bit too early for me but ...</td>
      <td>Cashier</td>
      <td>Whole Foods Market</td>
      <td>The pay is definitely more than average in New...</td>
    </tr>
    <tr>
      <th>80</th>
      <td>company is not doing well.</td>
      <td>Sr. Business Analyst</td>
      <td>Avon Products</td>
      <td>Good work life balance; professional work envi...</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Management was messy. \r\n\r\nTime Schedules w...</td>
      <td>Sales Associate</td>
      <td>Forever 21</td>
      <td>Lots of clothes and discounts</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Long Hours, Not enough help,</td>
      <td>Manager</td>
      <td>Bed Bath &amp; Beyond</td>
      <td>Culture, Co-Workers,Strong Management team, Cu...</td>
    </tr>
    <tr>
      <th>83</th>
      <td>As interns, they don't burden you with a lot o...</td>
      <td>Tools &amp; Automation Group (TAG) Intern</td>
      <td>CA Technologies</td>
      <td>Had an amazing intern experience. The company ...</td>
    </tr>
    <tr>
      <th>84</th>
      <td>1. Salary and Benefits\r\n2. Late Work Hours\r...</td>
      <td>Great Company</td>
      <td>Infosys</td>
      <td>1. Wide Array of Clients\r\n2. Scope to learn ...</td>
    </tr>
    <tr>
      <th>85</th>
      <td>No staff, no hours in budget, management can b...</td>
      <td>Tons of work, no staff or recognition.</td>
      <td>Walgreens</td>
      <td>Good pay, flexible scheduling, some of the peo...</td>
    </tr>
    <tr>
      <th>86</th>
      <td>No professional growth / no development strate...</td>
      <td>Fun Work, No Growth</td>
      <td>Saks Fifth Avenue</td>
      <td>Summer Fridays / beautiful offices / discounts</td>
    </tr>
    <tr>
      <th>87</th>
      <td>there is a lack of low diversity</td>
      <td>Research assistant</td>
      <td>Stony Brook University</td>
      <td>you will enjoy Flexible work time</td>
    </tr>
    <tr>
      <th>88</th>
      <td>The work schedule was hard to balance work and...</td>
      <td>admin  manager</td>
      <td>Lowe's</td>
      <td>The pay was very good. I was also eligible for...</td>
    </tr>
    <tr>
      <th>89</th>
      <td>They do not respect your work life balance. Ex...</td>
      <td>Good Company</td>
      <td>Tata Consultancy Services</td>
      <td>Gives a long term onsite opportunities.</td>
    </tr>
    <tr>
      <th>90</th>
      <td>No cons to report to other colleagues</td>
      <td>Great Global Company</td>
      <td>Unilever</td>
      <td>Only worked there a year but it was a great ex...</td>
    </tr>
    <tr>
      <th>91</th>
      <td>HR can be two-faced, they are there to "help,"...</td>
      <td>Nice people, Bad company</td>
      <td>Barnes &amp; Noble</td>
      <td>Excellent benefits (health insurance, paid vac...</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Management ignores ideas of employees</td>
      <td>Gold Choice Service Representative</td>
      <td>Hertz</td>
      <td>Being in a strong union is always good.</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Raises are only given in union stores , with p...</td>
      <td>Not a bad job , just could be better</td>
      <td>Rite Aid</td>
      <td>Most are willing to work with your schedule, e...</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Some projects (or client engagements) are not ...</td>
      <td>Great place to learn</td>
      <td>McKinsey &amp; Company</td>
      <td>Great place to learn at, they place a lot of e...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>I do not have any</td>
      <td>Working at Emblem</td>
      <td>EmblemHealth</td>
      <td>Good work environment\r\nNice People to work</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Can be difficult for the 'average employee' to...</td>
      <td>Emphasis on employee engagement</td>
      <td>Nielsen</td>
      <td>Large emphasis on employee well-being and enga...</td>
    </tr>
    <tr>
      <th>97</th>
      <td>micromanaging and manager was not understanding</td>
      <td>decent place to work at</td>
      <td>Capital One</td>
      <td>not pushy on numbers\r\ngood hours\r\neasy work</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Lack of career development help, lower compens...</td>
      <td>BNP Paribas review</td>
      <td>BNP Paribas</td>
      <td>Opportunity to learn many different businesses...</td>
    </tr>
    <tr>
      <th>99</th>
      <td>The pay is laughable at times.</td>
      <td>Good Company</td>
      <td>Tiffany &amp; Co.</td>
      <td>You never have to explain why you work here.</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>




```python

```


```python

```


```python

```
