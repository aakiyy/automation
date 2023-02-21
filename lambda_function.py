# coding: utf-8

import json
from commands import Command

'''
### event json
{
    "commands": [
        'SCRAPE_GOOGLE_TREND',
        'SCRAPE_GOOGLE_TREND',
        'SCRAPE_YOUTUBE_TREND'
    ]
}
'''

def lambda_handler(event, context):
    commands = event['commands']

    if Command.SCRAPE_GOOGLE_TREND.name in commands:
        print(Command.SCRAPE_GOOGLE_TREND.name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }