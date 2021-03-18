from checker import Checker

URL = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942'

class WalmartChecker(Checker):

	def __init__(self, url):
		super().__init__(URL)


if __name__ == "__main__":
	test = WalmartChecker(URL)
	test.get_soup()
	test.print_soup()