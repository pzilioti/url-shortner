# URL Shortner

This project is a url shortner. It's done in python using the django framework. It have 3 functionalities. First, a shortner, where the user submits an url and it's shortned. Second, a endpoint to consult the original url from a shortened url, and finally the redirection from the shortened url to the original website.


## Running

First makes sure your system have python installed:

    python -V

The response should be something like this:

    Python 3.8.5

After this, run the following commands in the folder of the project:

    python -m pip install -r requirements.txt
    python  manage.py  migrate
    python  manage.py  runserver

The project will start running in your localhost in port 8000

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Docker alternative

Or, if you're in a Linux environment with docker installed, just run the script deploy.sh

    ./deploy.sh
It'll start a docker instance listening in port 8000

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## How to use

The project have 3 endpoints.

 1. /short/?url={url}
The server receives the url, creates a short version and answers to the user this short version

 2. /long/?url={url}
The server receives the shortned url and gives back the original url along the click count, if the shortned url exists in the database

 3. /{short}
Redirects from the short url to the original website


## Demo

The project is running on my server.

[https://www.zilioti.dev/demo_shortner/](https://www.zilioti.dev/demo_shortner)

## Next steps




