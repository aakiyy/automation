# coding: utf-8

import json
from models.commands import Command
from parameter_store_client import ParameterStoreClient
from slack_client import SlackClient

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
    parameter_client = ParameterStoreClient()

    post_slack_message("C04QA9SQ8BD", "テストメッセージ", parameter_client)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    # if Command.SCRAPE_GOOGLE_TREND.name in commands:
    #     scrape_google_trends()
    # if Command.SCRAPE_TWITTER_TREND.name in commands:
    #     scrape_twitter_trends()
    # if Command.SCRAPE_YOUTUBE_TREND.name in commands:
    #     scrape_youtube_trends()

def post_slack_message(channel_id, message, parameter_client):
    slack_bot_token = parameter_client.get_parameter("/slack/daily_notification/bot_token")
    slack_client = SlackClient(slack_bot_token)
    slack_client.post_message(channel_id, message)

def scrape_google_trends():
    print(Command.SCRAPE_GOOGLE_TREND.name)
    pass 

def scrape_twitter_trends():
    print(Command.SCRAPE_TWITTER_TREND.name)
    pass

def scrape_youtube_trends(): 
    print(Command.SCRAPE_YOUTUBE_TREND.name)
    pass

