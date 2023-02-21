# coding: utf-8

import json
from models.commands import Command

# event json 
# {
#   "commands": [
#       'SCRAPE_GOOGLE_TREND',
#       'SCRAPE_TWITTER_TREND',
#       'SCRAPE_YOUTUBE_TREND'
#   ]
# }
def lambda_handler(event, context):
    commands = event['commands']

    results = {}

    if Command.SCRAPE_GOOGLE_TREND.name in commands:
        scrape_google_trends()
    if Command.SCRAPE_TWITTER_TREND.name in commands:
        scrape_twitter_trends()
    if Command.SCRAPE_YOUTUBE_TREND.name in commands:
        scrape_youtube_trends()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def scrape_google_trends():
    print(Command.SCRAPE_GOOGLE_TREND.name)
    pass 

def scrape_twitter_trends():
    print(Command.SCRAPE_TWITTER_TREND.name)
    pass

def scrape_youtube_trends(): 
    print(Command.SCRAPE_YOUTUBE_TREND.name)
    pass

