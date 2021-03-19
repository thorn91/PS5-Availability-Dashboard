'''
Webserver to serve requests of the status of the Playstation 5.
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from walmart_checker import WalmartChecker
from target_checker import TargetChecker

# Creates FastAPI instance
app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
)


@app.get('/')
async def root():
	''' Fake data '''
	return {"stock": True, "stock_date": "Mar 18 at 3:00 PM ET", "check_back": True}


@app.get('/walmart')
async def walmart():
	w = WalmartChecker()
	data = w.check_stock()

	return data

@app.get('/target')
async def target():
	''' Almost no scraping is involved.  Let the frontend deal with parsing JSON. '''
	t = TargetChecker()
	data = t.check_stock()

	return data['data']
