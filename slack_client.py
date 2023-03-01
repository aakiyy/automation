import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    def __init__(self, slack_bot_token):
        self.slack_bot_token = slack_bot_token

    def post_message(self, channel_id, text):
        client = WebClient(token = self.slack_bot_token)
        try:
            result = client.chat_postMessage(channel = channel_id, text = text)
            print(result)
        except SlackApiError as e:
            print(f"Error posting message: {e}")
