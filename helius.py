import requests

URL = "https://mainnet.helius-rpc.com/?api-key="


class Helius:
    def __init__(self, api_key):
        self.__api_key = api_key
        pass

    def get_holders(self, page, address):
        resp = requests.post(
            url=URL+self.__api_key,
            json={
                "jsonrpc": "2.0",
                "method": "getTokenAccounts",
                "id": "helius-test",
                "params": {
                    "page": page,
                    "limit": 1000,
                    "displayOptions": {},
                    "mint": address,
                },
            },
            headers={
                "Content-Type": "application/json",
            }
        )
        return resp.json()['result']['token_accounts']


if __name__ == '__main__':
    x = Helius(
        '3c7f83a9-a972-44bf-b442-90f4861aae97'
    )
    print(x.get_holders(1, 'AFivsHqtajxcbQmyuZ7TQymx1ypSs6S74dLEY4BGRxXf'))