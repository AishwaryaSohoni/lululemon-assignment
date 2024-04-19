Hey there! This is my submission for the Web Scraper Assignment.

## How to run the scraper
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Run django server using `python manage.py runserver`

## What has been implemented?
I was able to manage scrape just the first url. 
Setting up the repo, django project, unit tests etc took a while.
I was not able to scrape the other URL. I also have not implemented any persistence layer for the caching, 
just plain and simple in-memory cache.

## What would I have done if I had more time?
- I would have implemented the persistence layer for the cache.
- Defined a model for the scraped data. Serializers etc
- Installed isort, black, flake8 for linting and formatting
- Implemented the second URL scraping
- Tried to set this up in a docker container and then export the container to AWS lambda using SAM
