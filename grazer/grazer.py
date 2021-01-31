import os
import alpaca_trade_api as alpaca


PAPER_URL = 'https://paper-api.alpaca.markets'
LIVE_URL = 'https://api.alpaca.markets'

class Grazer(object):

    def __init__(self, key_file, live=False):
        self._client = None
        self.load_keys_from_file(key_file, live)

    def load_keys_from_file(self, key_file, live=False):

        if not os.path.exists(key_file):
            raise FileNotFoundError(f"{key_file} does not exist")

        with open(key_file, 'r') as f:
            [key_id, secret_key] = f.readlines()[:2]
            url = PAPER_URL
            if live:
                url = LIVE_URL
            self._client = alpaca.REST(key_id, secret_key, base_url=url)

