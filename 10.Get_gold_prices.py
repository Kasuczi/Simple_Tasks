import json
import requests
import matplotlib.pyplot as plt


class NbpApi:
    GOLD_PRICE_URL = 'http://api.nbp.pl/api/cenyzlota?format=json'
    GOLD_LAST_TOP_COUNT_URL = (
        'http://api.nbp.pl/api/cenyzlota/last/{top_count}?format=json'
    )

    def make_request(self, url):
        """
        The func creates a request to the website
        """
        res = requests.get(url)
        return json.loads(res.content)

    def get_gold_price(self):
        """
        The func returns a price of gold
        """
        res = self.make_request(self.GOLD_PRICE_URL)
        return res[0]['cena']

    def get_gold_last_count(self, top_count):
        res = self.make_request(
            self.GOLD_LAST_TOP_COUNT_URL.format(top_count=top_count)
        )
        return res

def is_gold_expensive(treshold):
    """
    The func returns True if gold value is above treshold otherwise False
    """
    nbp_api = NbpApi()
    if nbp_api.get_gold_price() > treshold:
        return True
    return False

def gold_change_percentage(top_count):
    """
    The func retruns % of changed value
    """
    nbp_api = NbpApi()
    data = nbp_api.get_gold_last_count(top_count)
    percentage = (data[-1]['cena'] - data[0]['cena']) / data[0]['cena']* 100
    return percentage

def gold_diagram_last_month():
    """
    The func returns a plot with a price of gold in the timeline
    """
    nbp_api = NbpApi()
    data = nbp_api.get_gold_last_count(10)
    x = [data_dict['data'] for data_dict in data]
    y = [data_dict['cena'] for data_dict in data]
    plt.plot(x, y)
    plt.show()

gold_diagram_last_month()
