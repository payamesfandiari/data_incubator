# Data Incubator Project

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Datasets and proposal
##Motivation : 
When I came to United States, I wanted to live in NYC specifically Manhattan. It's now three years after I came here and I could not live in Manhattan for one day. One of the most important reason for this is that I get scared everytime I think about moving to NYC because of the sheer amount of information and pitfalls. You have to think about every aspect of your livelihood in order to find a good neighborhood and a perfect place you could call home ! 
This motivated me to create a system that can recommend a place. Just like other Recommendation and Ranking systems, one can design a system based on the huge amount of data that is available online. So I decided to create a new "Recommendation System for Housing" which I call "NYC Demystify"

##Description : 
We start by mining and gathering the data required for the project. We Create a dataset of "Borough"s and "Neighbourhoods". Then for each one of them we create a feature vector based on these parameters : 
```Air pollution measurement
Water pollution measurement
number of restaurants
number of cafes
number of bars
avg rating of restaurants
avg rating of cafes
avg rating bars
number of schools
number of colleges
number of parking lots
number of parking spots on the street
number of Farmer's market
number of Wholefoods/trader's joe
number of other supermarkets and grocery stores 
number of art centers
number of parks
number of collisions resulted in death
number of other kinds of collisions 
number of crimes happened in the area
Also, we append fractions of these measures based on the population.
Also, we use KNearestNeighbour to find the distances of the center of a Neighbourhood to top 10 best restaurants and bars and cafe based on user input from Yelp
```
The first step in this project is extracting some information from these data. In the first plot you can see that based on these features Brooklyn has better score which was surprising. Specifically it seems that the number of businesses and the Avg rating of them are much higher than Manhattan. 
Also I decided not to put any weight on the features at this time. In the next step these weighting will come from the User. 
In the next plot you can see that overall the number of Point of Interest are much higher in Brooklyn despite the usual believe ! 

##Data
The data for this project comes from several sources. Here is a list of datasets I used for this project : 
Legally Operating Businesses : 
         https://data.cityofnewyork.us/Business/Legally-Operating-Businesses/w7w3-xahh
CDC Annual Health Data :
         https://www.cdc.gov/brfss/annual_data/2015/files/LLCP2015ASC.zip
Street Assessment Testing :
        https://data.cityofnewyork.us/api/views/umhe-raak
Outdoor Air and Health Info : 
        https://data.cityofnewyork.us/api/views/c3uy-2p5r
NYC neighbourhood names : 
        https://data.cityofnewyork.us/api/assets/EADEB66A-87D5-4E9E-8D68-A1B9049F6EE8?download=true
Water Quality complaints :
       https://data.cityofnewyork.us/api/views/INLINE/rows.csv?accessType=DOWNLOAD
NYC Taxi Data (Not used in this step): 
      http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
Historical New York City Crime Data  :     http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/citywide_historical_crime_data_archive.zip

APIs :
      Google Place Web Service API
      Yelp Business Search API
      OpenData Socrata API

##Next Step : 
The next step is consists of several steps : 
first, include a ranking system so people could rank their neighbourhood easily. 
second, Create a Deep Belief Network to implement a Recommender System. Altough recommender systems like Restricted Boltzman Machine of Netflix have been at work but I think Deep Learning methods are game changers. 
(Good starting point : https://arxiv.org/pdf/1409.2944.pdf )
third, extend the project to other cities. 


