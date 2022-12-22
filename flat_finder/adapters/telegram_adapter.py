import os

import requests

from flat_finder.models import AbstractAdapter, ParsedFlat


class TelegramAdapter(AbstractAdapter):

    def __init__(self):
        self.token = os.environ['TELEGRAM_BOT_TOKEN']
        self.chat_id = os.environ['TELEGRAM_CHAT_ID']

    def send_flat(self, flat: ParsedFlat) -> bool:
        message = f"[{flat.title}]({flat.link})\n" \
                        + f"{flat.price}\n" \
                        + f"{flat.size}\n" \
                        + f"{flat.address}\n"

        response = requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}&parse_mode=Markdown')

        return response.status_code // 100 == 2