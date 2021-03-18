'''
Parent class of all specific company webscrapers.  Contains (most) the parameters
and methods needed to basically scrape any non-JS heavy site.
'''

from bs4 import BeautifulSoup
from os import path
import requests
import logging


class Checker:

	def __init__(self, url):
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

	def _setup_logger(self):
		# Ensure namespace passes to child
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
			Note: request.get() is blocking so async will have to be handled on the server
		'''
		try:
			self.res = requests.get(self.url)
			self.res.raise_for_status()   # raises HTTPError
			self.logger.info(f'Request successful to {self.url}')
			self.soup = self.res.content
			
			return True
			
		except requests.HTTPError as e:
			self.logger.error(f'ERROR: Request failed to {self.url}')
			return False
	
	def print_soup(self):
		''' Helper method to print the HTML contents '''
		if self.soup != None:
			print(self.soup)
		else:
			self.logger.error('Unable to print soup.')


if __name__ == "__main__":
	test = Checker('https://www.google.com')
	test.get_soup()			
		

