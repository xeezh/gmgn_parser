from curl_cffi import requests


class GmGnApi:
    def __init__(self):
        self.__session = requests.Session(
            impersonate='chrome124'
        )
        self.__session.headers = self.__get_headers()
        self.__init_session()

    def __init_session(self):
        self.__session.get(
            url="https://gmgn.ai/"
        )

    def __get_headers(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.7',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
        }
        return headers

    def get_wallet_data(self, address):
        response = self.__session.get(
            url=f'https://gmgn.ai/defi/quotation/v1/smartmoney/sol/walletNew/{address}',
            params={
                'period': '30d',
            },
            headers=self.__get_headers(),
        )
        j = response.json()
        data_full = j['data']
        data = {
            'pnl': data_full['pnl_30d'] if data_full['pnl_30d'] is not None else 0,
            'profit': data_full['realized_profit_30d'] if data_full['realized_profit_30d'] is not None else 0,
            'winrate': data_full['winrate'] if data_full['winrate'] is not None else 0,
            'tradesize': data_full['token_avg_cost'] if data_full['token_avg_cost'] is not None else 0
        }
        return data






