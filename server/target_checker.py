'''
Target renders most of their information with JS/AJAX so it can't just be scraped.
Fortunately, redsky accepts a store position, store id, and product ID and will return
store availability.
'''
from checker import Checker
import requests
import json


class TargetChecker(Checker):

	def __init__(self, url=None):
		''' 
		Target CANNOT accept custom URLs, it is way too much of a pain to dig through the Network Inspector.
		'''
		URL = 'https://redsky.target.com/redsky_aggregations/v1/web/pdp_fulfillment_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&tcin=81114595&store_id=1453&store_positions_store_id=1453&has_store_positions_store_id=true&zip=30606&state=GA&latitude=33.960&longitude=-83.450&pricing_store_id=1453'

		super().__init__(URL)

	def get_contents(self):
		''' Method override: we do not need BS4, this is JSON data '''
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
		self.res = requests.get(self.url, headers).json()

	def check_stock(self):
		''' There is no scraping involved, so we should handle the JSON parsing on the front end '''

		return self.res

		

if __name__ == "__main__":
	test = TargetChecker()
	# test.print_html()
	test.check_stock()