# PS5 Availability Tracker

Tired of scalpers beating you to a PS5 before you even know they're in stock?  With this app, you can get real time updates scraped directly from big box retail website to help you fail at actually being able to add it to your cart and checkout.  

Make frustration more frantic and just maybe, hopefully, beat out a scalper or two.

Ironically, I found a PS5 late at Sam's club while setting up their module.  So I guess this worked after all.

# Stores Curated

Disclaimer: no terms of service or Robots.txt rules were violated in _any_ of these searches. Everything is above board, legal, and done through official APIs whenever possible.

- [x] Walmart
- [x] Target
- [x] Sam's club

# Features

## Backend: Python REST Server with FastAPI

* Official APIs used whenever possible, JS avoidance tactics with browser automation completely avoided
* Each store response customized to account for all situations (such as target giving local availability or Walmart giving exact dates/times of their next restock/refresh)
* Simple but performant webserver is easily modifiable sends mostly filtered JSON data to the front end, taking the load off your browser
* Specific webscrapers inherit from the simple parent Checker class, allowing customization for the next hot product (GPU's anyone?)

## Frontend: Vue.js SPA with Axios and Bootstrap

* Easy to understand and easy to extend.  Vue components need to be improved, as I didn't realize that different stores provide different information, such as Target providing individual store availability information along with overall shipping, or Walmart providing specific dates, which led to each store essentially becoming its own component despite the shared features.

![image](demo/demo.png)

## Project setup
```
npm install
```

### Compiles and hot-reloads for development from inside `ps5-dashboard`
```
npm run serve 
```

### Python setup from inside `server`
```
pip install -r requirements.txt
```

### Starts the Python webserver from inside `server`
```
uvicorn server:app --reload
```

### Start both servers at once

I don't really recommend this unless you just plan on closing your terminal right after.
Replace zsh with what is appropriate for your system.  A build script is coming soon!

```
zsh -c "cd server && uvicorn server:app --reload; cd ps5_dashboard && npm run serve" & > output.txt &
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
