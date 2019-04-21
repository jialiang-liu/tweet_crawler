#  Twitter Stream
Team: this_is_a_team  

# Installation

# 1 To run Tweepy streamer:  
1. Create a twitter account and apply for twitter developer account  
2. After creating an account, find your api key, secret key, access token, and secret token under Keys and Access Tokens and add to tweet_stream.py  
3. sudo pip install tweepy to install tweepy  
4. Run python tweet_stream.py  
5.  Collected tweets will be stored in a file named 'final.json'

# 2 To install Elasticsearch:  
1. Go to https://www.elastic.co/downloads/elasticsearch
2. Download and unzip the file
3. Run  
`cd elasticsearch-6.6.2/bin`  
`./elasticsearch`  

To install libraries   
`pip3 install elasticsearch`  
Run to build the index idx_twp and mapping  
`curl -X PUT "localhost:9200/idx_twp" -H 'Content-Type: application/json' -d' \n 
{  \n
  "mappings": {  
    "twitter_twp": {  
      "properties": {  
        "location": {  
          "type": "geo_point"  
        }  
      }  
    }  
  }  
}  
'  `  
`python3 index.py`
These two command run the python file to build the index based on the json file

# 3 To install Kibana  
1. Go to https://www.elastic.co/downloads/kibana 
2. Download and unzip
3. Run  
`cd kibana-6.6.2-windoes-x86_64\bin`  
`./kibana.bat`  

# 4 open the chrome go to `localhost:5601`  
1. Go to "Management" -> "Kibana" -> "Index Patterns" -> "Create index patter" -> enter "idx_twp" -> Next step -> Next step  
We would able to create the index that we created at elasticsearch in Kibana.
2. Go to "Visualize" -> "Create a Visualization" -> "Coordinate Map" -> select "idx_twp" -> "Bucket"-> "Geo Coordinates" -> "Field" -> "location" -> click "Apply changes"  
3. Kibana would make the twitter visualize for you


