'''
Parent class of all specific company webscrapers.  Contains (most) the parameters
and methods needed to basically scrape any non-JS heavy site.
'''

from bs4 import BeautifulSoup
from os import path
import requests
import logging
import json


class Checker:

	def __init__(self, url=None):
		'''
			Initial setup.  There are a lot of varying things between the sites, so for
			most of these it may be impossible to simply pass in a few arguments and
			get a True/False for the stock.  It is easier to just standardize making
			the scrapable soup and deal with the intricacies on a case-by-case basis.

			url: the product url page
		'''
		self.url = url

		# Setup logger
		self.logger = None
		self._setup_logger()

		# Request and BS4 result will be ready for scraping
		self.res = None
		self.soup = None
		self.data = {}  # Return data for the API

		# Go ahead and get the request, there is no reason to wait as of now
		self.get_contents()

	def _setup_logger(self):
		''' Basic logger setup.  Uses the filename to tell which scraper is logged. '''
		logging.basicConfig(
			format = f'{path.basename(__file__)} %(asctime)s %(message)s',
   			datefmt = '%m/%d/%Y %I:%M:%S %p',
            filename = 'app.log',
            level=logging.DEBUG
		)

		self.logger = logging.getLogger(__name__)
		
		
	def get_contents(self):
		''' 
			Passes the contents of a get request into a bs4 parser.  
			Note: request.get() is blocking so async will have to be handled on the server.g
		'''
		try:
			# Ensure headers to bypass initial bot security, I would rather not use selenium
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
			self.res = requests.get(self.url, headers=headers)
			self.res.raise_for_status()   # raises HTTPError
			self.logger.info(f'Request successful to {self.url}')
			self.soup = BeautifulSoup(self.res.text, features="html.parser")
			
			return True
			
		except requests.HTTPError as e:
			self.logger.error(f'ERROR: Request failed to {self.url}')

			return False
	
	def print_html(self):
		''' Helper method to print the HTML contents nicely. '''
		if self.soup != None:
			print(self.soup.prettify())
		else:
			print('Unable to print - check request status.')

	def get_json(self):
		if self.data != {}:
			print(type(json.dumps(self.data)))
			return json.dumps(self.data)
		else:
			logger.error("JSON data object is empty")
			return {}


if __name__ == "__main__":
	test = Checker('https://www.google.com')
	test.get_soup()			
		

