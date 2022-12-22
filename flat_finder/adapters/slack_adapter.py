from flat_finder.models import AbstractAdapter, ParsedFlat

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackAdapter(AbstractAdapter):

    def __init__(self):
        self.client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
        self.channel = os.environ['SLACK_BOT_CHANNEL']
        self.username = "pythonboardingbot"
        self.icon_emoji = ":robot_face:"

    def send_flat(self, flat: ParsedFlat) -> bool:
        message = f"*<{flat.link}|{flat.title}>*\n" \
                        + f"{flat.price}\n" \
                        + f"{flat.size}\n" \
                        + f"{flat.address}\n"

        try:
            response = self.client.chat_postMessage(
                channel=self.channel,
                username=self.username,
                mrkdwn=True,
                icon_emoji=self.icon_emoji,
                text=message)
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")
            return False

        if response.status_code // 100 != 2:
            print(f"Error sending to Slack: {response.status_code}")
            return False

        return True
