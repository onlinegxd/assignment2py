from requests import Session
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '54027113-f309-4184-8950-3d1f53aca5dd'
}

session = Session()
session.headers.update(headers)


class MyCryptoWallet:
    def __init__(self, curr, amount):
        self.curr = curr
        self.amount = amount

    def getcurrentprice(self):
        parameterscurrent = {
            'slug': self.curr,
            'convert': 'USD'
        }
        response = session.get(url, params=parameterscurrent)

        for x in json.loads(response.content)['data']:
            price = json.loads(response.content)['data'][x]['quote']['USD']['price'] * self.amount

        return price


def exchangetogiven(ex1, givencurr):
    ex2 = MyCryptoWallet(givencurr, 1)
    diff = ex1.getcurrentprice()/ex2.getcurrentprice()
    return diff
