import requests
from bs4 import BeautifulSoup
from FinanceModules.processing import Processing

class ScrapingData:

    def __init__(self, url):
        request = requests.get(url)
        got_bs =BeautifulSoup(request.content, "lxml")
        self.got_html = got_bs


    def exchange_usdjpy(self):
        find_price_tag = Processing().find_html_id(self.got_html, "USDJPY_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_eurjpy(self):
        find_price_tag = Processing().find_html_id(self.got_html, "EURJPY_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_gbpjpy(self):
        find_price_tag = Processing().find_html_id(self.got_html, "GBPJPY_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_eurusd(self):
        find_price_tag = Processing().find_html_id(self.got_html, "EURUSD_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_usdchf(self):
        find_price_tag = Processing().find_html_id(self.got_html, "USDCHF_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_gbpusd(self):
        find_price_tag = Processing().find_html_id(self.got_html, "GBPUSD_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)


    def exchange_eurgbp(self):
        find_price_tag = Processing().find_html_id(self.got_html, "EURGBP_detail_bid")
        bid_price = Processing().get_price_text(find_price_tag)
        return float(bid_price)