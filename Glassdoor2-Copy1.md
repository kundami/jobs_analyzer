

```python
import requests 
import json
#from glassdoor import get
url= "https://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=199084&t.k=D3Ee1oQ6L9&action=employers&q=pharmaceuticals&userip=10.0.0.133"
print(url)
headers = {'user-agent': 'Mozilla/5.0'}
response=requests.get(url, headers=headers).json()

print(json.dumps(response,indent=2))
```

    https://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=199084&t.k=D3Ee1oQ6L9&action=employers&q=pharmaceuticals&userip=10.0.0.133
    {
      "success": true,
      "status": "OK",
      "jsessionid": "5B39190A2E658D1A5C4E68A460344A1D",
      "response": {
        "attributionURL": "https://www.glassdoor.com/Reviews/pharmaceuticals-reviews-SRCH_KE0,15.htm",
        "currentPageNumber": 1,
        "totalNumberOfPages": 109,
        "totalRecordCount": 1089,
        "employers": [
          {
            "id": 18697,
            "name": "Novartis Pharmaceuticals",
            "website": "www.pharma.us.novartis.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 945,
            "squareLogo": "https://media.glassdoor.com/sqll/18697/novartis-pharmaceuticals-squarelogo.png",
            "overallRating": "3.8",
            "ratingDescription": "Satisfied",
            "cultureAndValuesRating": "3.6",
            "seniorLeadershipRating": "3.2",
            "compensationAndBenefitsRating": "3.6",
            "careerOpportunitiesRating": "3.4",
            "workLifeBalanceRating": "3.5",
            "recommendToFriendRating": 71,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Novartis-Pharmaceuticals-RVW16926853.htm",
              "id": 16926853,
              "currentJob": false,
              "reviewDateTime": "2017-09-20 10:32:26.46",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Finance department",
              "pros": "Great staff, so friendly and helpful",
              "cons": "None really, just your typical reporting to higher management struggles",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Andr\u00e9 Wyss",
              "title": "President",
              "numberOfRatings": 256,
              "pctApprove": 81,
              "pctDisapprove": 19,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/18697/novartis-pharmaceuticals-andr\u00e9-wyss.png",
                "height": 195,
                "width": 200
              }
            }
          },
          {
            "id": 6440,
            "name": "Teva Pharmaceuticals",
            "website": "www.tevapharm.com",
            "isEEP": true,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 707,
            "squareLogo": "https://media.glassdoor.com/sqll/6440/teva-pharmaceuticals-squarelogo.png",
            "overallRating": "3.3",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "3.3",
            "seniorLeadershipRating": "2.8",
            "compensationAndBenefitsRating": "3.7",
            "careerOpportunitiesRating": "3.0",
            "workLifeBalanceRating": "3.3",
            "recommendToFriendRating": 60,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Teva-Pharmaceuticals-RVW16843829.htm",
              "id": 16843829,
              "currentJob": false,
              "reviewDateTime": "2017-09-15 07:52:05.067",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Great place to work, room for advancement",
              "pros": "Company provides good salary and excellent benefits package",
              "cons": "Closing New York and Virginia sites",
              "overall": 4,
              "overallNumeric": 4
            },
            "ceo": {
              "name": "Yitzhak Peterburg",
              "title": "Interim President & CEO",
              "numberOfRatings": 36,
              "pctApprove": 49,
              "pctDisapprove": 51,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/6440/teva-pharmaceuticals-ceo1487099716737.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 7774,
            "name": "Takeda Pharmaceuticals",
            "website": "www.takedajobs.com",
            "isEEP": true,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 681,
            "squareLogo": "https://media.glassdoor.com/sqll/7774/takeda-pharmaceuticals-squarelogo-1496324580544.png",
            "overallRating": "3.4",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "3.3",
            "seniorLeadershipRating": "2.8",
            "compensationAndBenefitsRating": "3.6",
            "careerOpportunitiesRating": "2.8",
            "workLifeBalanceRating": "3.5",
            "recommendToFriendRating": 57,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Takeda-Pharmaceuticals-RVW16893485.htm",
              "id": 16893485,
              "currentJob": false,
              "reviewDateTime": "2017-09-18 19:34:51.507",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Pharmacoepidemiology Intern",
              "pros": "Require good understanding of epidemiology and writing skills",
              "cons": "I didn't find any cons",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Christophe Weber",
              "title": "President and CEO",
              "numberOfRatings": 143,
              "pctApprove": 75,
              "pctDisapprove": 25,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/7774/takeda-pharmaceuticals-ceo1488175903093.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 38454,
            "name": "Boehringer Ingelheim Pharmaceuticals",
            "website": "us.boehringer-ingelheim.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 498,
            "squareLogo": "https://media.glassdoor.com/sqll/38454/boehringer-ingelheim-pharmaceuticals-squarelogo.png",
            "overallRating": "3.3",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "3.0",
            "seniorLeadershipRating": "2.6",
            "compensationAndBenefitsRating": "3.4",
            "careerOpportunitiesRating": "2.8",
            "workLifeBalanceRating": "3.6",
            "recommendToFriendRating": 55,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Boehringer-Ingelheim-Pharmaceuticals-RVW16862017.htm",
              "id": 16862017,
              "currentJob": false,
              "reviewDateTime": "2017-09-16 17:11:53.233",
              "jobTitle": "Employee",
              "location": "Ridgefield, CT",
              "headline": "Exciting science",
              "pros": "Great people. Exciting research and discovery group. Potential for development",
              "cons": "Two year rule for contract jobs",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Dr Andreas Barner",
              "title": "Chairman of the Board",
              "numberOfRatings": 155,
              "pctApprove": 62,
              "pctDisapprove": 38,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/38454/boehringer-ingelheim-pharmaceuticals-dr-andreas-barner.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 981,
            "name": "Regeneron Pharmaceuticals",
            "website": "www.regeneron.com",
            "isEEP": true,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 376,
            "squareLogo": "https://media.glassdoor.com/sqll/981/regeneron-pharmaceuticals-squarelogo-1452804357483.png",
            "overallRating": "3.7",
            "ratingDescription": "Satisfied",
            "cultureAndValuesRating": "3.9",
            "seniorLeadershipRating": "3.6",
            "compensationAndBenefitsRating": "3.8",
            "careerOpportunitiesRating": "3.5",
            "workLifeBalanceRating": "3.3",
            "recommendToFriendRating": 74,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Regeneron-Pharmaceuticals-RVW16935340.htm",
              "id": 16935340,
              "currentJob": false,
              "reviewDateTime": "2017-09-20 18:02:18.483",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Intern",
              "pros": "free shuttle to north white plains\r\ngreat work culture\r\nfun activities during summer",
              "cons": "no gym for summer interns",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Leonard S. Schleifer",
              "title": "President, CEO, and Director",
              "numberOfRatings": 256,
              "pctApprove": 94,
              "pctDisapprove": 6,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/981/regeneron-pharmaceuticals-leonard-s-schleifer.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 11717,
            "name": "Janssen",
            "website": "www.janssen.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 320,
            "squareLogo": "https://media.glassdoor.com/sqll/11717/janssen-squarelogo.png",
            "overallRating": "3.8",
            "ratingDescription": "Satisfied",
            "cultureAndValuesRating": "4.0",
            "seniorLeadershipRating": "3.2",
            "compensationAndBenefitsRating": "3.7",
            "careerOpportunitiesRating": "3.2",
            "workLifeBalanceRating": "3.6",
            "recommendToFriendRating": 81,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "parentEmployer": {
              "id": 364,
              "name": "Johnson & Johnson",
              "relationshipDate": "",
              "relationship": "SUBSIDIARYOF",
              "isSunset": false,
              "sunsetMessage": "",
              "logo": {
                "normalUrl": "https://media.glassdoor.com/sql/364/johnson-and-johnson-squarelogo.png",
                "mediumUrl": "https://media.glassdoor.com/sqlm/364/johnson-and-johnson-squarelogo.png",
                "smallUrl": "https://media.glassdoor.com/sqls/364/johnson-and-johnson-squarelogo.png"
              }
            },
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Janssen-RVW16812784.htm",
              "id": 16812784,
              "currentJob": true,
              "reviewDateTime": "2017-09-13 15:33:43.107",
              "jobTitle": "Scientist",
              "location": "",
              "jobTitleFromDb": "Scientist",
              "headline": "Great Place to Work",
              "pros": "Relaxed, family orientated, dog-friendly company.  Retained some of its small company culture after it was acquired by J&J.  Great benefits!",
              "cons": "Typically big pharma issues and \"busy work\" with endless mandatory online training.  Can get tedious, but overall, nothing significant to complain about.",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Alex Gorsky",
              "title": "CEO",
              "numberOfRatings": 65,
              "pctApprove": 99,
              "pctDisapprove": 1,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/11717/janssen-ceo1474662430032.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 2080,
            "name": "Vertex Pharmaceuticals",
            "website": "www.vrtx.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 254,
            "squareLogo": "https://media.glassdoor.com/sqll/2080/vertex-pharmaceuticals-squarelogo.png",
            "overallRating": "3.4",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "3.7",
            "seniorLeadershipRating": "3.3",
            "compensationAndBenefitsRating": "4.4",
            "careerOpportunitiesRating": "3.2",
            "workLifeBalanceRating": "3.3",
            "recommendToFriendRating": 66,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Vertex-Pharmaceuticals-RVW16890476.htm",
              "id": 16890476,
              "currentJob": false,
              "reviewDateTime": "2017-09-18 15:54:48.333",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Awesome Company",
              "pros": "Great Company. Great science and great people.",
              "cons": "Nothing bad to say. I had the best time working for this company.",
              "overall": 5,
              "overallNumeric": 5
            },
            "ceo": {
              "name": "Jeffrey Leiden, M.D., Ph.D",
              "title": "President and CEO",
              "numberOfRatings": 105,
              "pctApprove": 71,
              "pctDisapprove": 29,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/2080/vertex-pharmaceuticals-jeffrey-leiden-m-d-ph-d.png",
                "height": 200,
                "width": 200
              }
            }
          },
          {
            "id": 669747,
            "name": "Mallinckrodt Pharmaceuticals",
            "website": "www.mallinckrodt.com",
            "isEEP": false,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 253,
            "squareLogo": "https://media.glassdoor.com/sqll/669747/mallinckrodt-squarelogo-1403292074724.png",
            "overallRating": "2.5",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "2.5",
            "seniorLeadershipRating": "2.2",
            "compensationAndBenefitsRating": "3.4",
            "careerOpportunitiesRating": "2.3",
            "workLifeBalanceRating": "2.9",
            "recommendToFriendRating": 29,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Mallinckrodt-Pharmaceuticals-RVW16886436.htm",
              "id": 16886436,
              "currentJob": true,
              "reviewDateTime": "2017-09-18 12:23:01.48",
              "jobTitle": "Senior IT Auditor",
              "location": "Saint Louis, MO",
              "jobTitleFromDb": "Senior IT Auditor",
              "headline": "Middle of the road",
              "pros": "Competitive starting salaries and base pay. Good flexibility",
              "cons": "moving towards outsourced model, instability and constantly understaffed",
              "overall": 3,
              "overallNumeric": 3
            },
            "ceo": {
              "name": "Mark Trudeau",
              "title": "President and Chief Executive Officer",
              "numberOfRatings": 120,
              "pctApprove": 25,
              "pctDisapprove": 75
            }
          },
          {
            "id": 6092,
            "name": "Alexion Pharmaceuticals",
            "website": "www.alxn.com",
            "isEEP": true,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 228,
            "squareLogo": "https://media.glassdoor.com/sqll/6092/alexion-pharmaceuticals-squarelogo.png",
            "overallRating": "2.5",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "2.6",
            "seniorLeadershipRating": "2.4",
            "compensationAndBenefitsRating": "4.0",
            "careerOpportunitiesRating": "2.6",
            "workLifeBalanceRating": "2.5",
            "recommendToFriendRating": 41,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Alexion-Pharmaceuticals-RVW16861099.htm",
              "id": 16861099,
              "currentJob": true,
              "reviewDateTime": "2017-09-16 14:44:19.573",
              "jobTitle": "Employee",
              "location": "",
              "headline": "Alexion",
              "pros": "Employees friendly environment. Good Salary Package",
              "cons": "Any employee can be terminated any time",
              "overall": 3,
              "overallNumeric": 3
            },
            "ceo": {
              "name": "Ludwig Hantson",
              "title": "Chief Executive Officer",
              "numberOfRatings": 18,
              "pctApprove": 70,
              "pctDisapprove": 30
            }
          },
          {
            "id": 343,
            "name": "Valeant",
            "website": "www.valeant.com",
            "isEEP": true,
            "exactMatch": false,
            "industry": "Biotech & Pharmaceuticals",
            "numberOfRatings": 201,
            "squareLogo": "https://media.glassdoor.com/sqll/343/valeant-squarelogo-1387302716008.png",
            "overallRating": "2.6",
            "ratingDescription": "OK",
            "cultureAndValuesRating": "2.3",
            "seniorLeadershipRating": "2.2",
            "compensationAndBenefitsRating": "3.2",
            "careerOpportunitiesRating": "2.4",
            "workLifeBalanceRating": "2.7",
            "recommendToFriendRating": 36,
            "sectorId": 10005,
            "sectorName": "Biotech & Pharmaceuticals",
            "industryId": 200021,
            "industryName": "Biotech & Pharmaceuticals",
            "featuredReview": {
              "attributionURL": "https://www.glassdoor.com/Reviews/Employee-Review-Valeant-RVW16800412.htm",
              "id": 16800412,
              "currentJob": true,
              "reviewDateTime": "2017-09-13 05:16:57.167",
              "jobTitle": "Employee",
              "location": "Bridgewater, NJ",
              "headline": "Positive Turnaround",
              "pros": "The culture for  those who work side by side (excluding the leadership tier) is inviting and motivating.  Everyone is incredibly invested in the turnaround of the company and hopeful for the future.",
              "cons": "We are still a lean company and internal communication (from manager to directs) still needs work. When priorities change at the drop of a hat and the new objective is not communicated properly, it causes a lot of frustration.",
              "overall": 4,
              "overallNumeric": 4
            },
            "ceo": {
              "name": "Joseph C. Papa",
              "title": "Chairman & CEO",
              "numberOfRatings": 30,
              "pctApprove": 68,
              "pctDisapprove": 32,
              "image": {
                "src": "https://media.glassdoor.com/people/sqll/343/valeant-ceo1467017342480.png",
                "height": 199,
                "width": 200
              }
            }
          }
        ]
      }
    }
    


```python

```
