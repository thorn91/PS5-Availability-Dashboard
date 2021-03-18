'''
Webserver to serve requests of the status of the Playstation 5.
'''

from fastapi import FastAPI

# Creates FastAPI instance
app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World"}


