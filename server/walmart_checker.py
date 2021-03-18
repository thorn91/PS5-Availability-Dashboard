from checker import Checker
import json


class WalmartChecker(Checker):

	def __init__(self, url=None):
		# Allow custom URLs
		URL = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942'
		if url:
			URL = url

		super().__init__(URL)

	def check_stock(self):
		''' Walmart actually tells when the next restock is. '''
		# Item is in stock
		if info := self.soup.find(class_='spin-button-children'):
			
			self.data['stock'] = True
			self.data['stock_date'] = ''
			self.data['check_back'] = False

			return self.data

		# There is a message other than "add to cart"
		if (stock_date := self.soup.find(class_='prod-blitz-copy-message').get_text()):

			if "will be back" in stock_date:
				# Item is in stock but they are reserving some
				self.data['stock'] = True
				self.data['stock_date'] = stock_date
				self.data['check_back'] = True

			elif "out of stock" in stock_date:
				# Item is completely out of stock
				self.data['stock'] = False
				self.data['stock_date'] = stock_date
				self.data['check_back'] = False

			else:
				# Item will be in stock at a specific date
				stock_date = stock_date.split(',')  # Remove first half
				stock_date = stock_date[1].strip()[:20]

				self.data['stock'] = False;
				self.data['stock_date'] = stock_date
				self.data['check_back'] = True

			return self.data


if __name__ == "__main__":
	test = WalmartChecker()
	# test.print_html()
	test.check_stock()