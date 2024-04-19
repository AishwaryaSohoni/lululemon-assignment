Hey there! This is my submission for the Web Scraper Assignment.

## How to run the scraper
1. Clone the repository
2. Import project into pycharm or the like
3. Set up a run configuration with the following parameters:
    - Working directory: <path-to-lulu_scraper>
    - Environment variables: `PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=settings`
3. Run this configuration

Note : Traditionally, I would install the dependencies in requirements.txt and the run the Django server using 
`python manage.py runserver`. However, while setiing the project up, I think I messed some config up while moving things
around. At the moment, I am not able to run the server using command line.
But it does run using the run configuration in PyCharm.

## What has been implemented?
I was able to scrape just the first url. 
Setting up the repo, django project, unit tests etc took a while.
I was not able to scrape the other URL. I also have not implemented any persistence layer for the caching, 
just plain and simple in-memory cache.

## What would I have done if I had more time?
- I would have implemented the persistence layer for the cache.
- Defined a model for the scraped data. Serializers etc
- Installed isort, black, flake8 for linting and formatting
- Implemented the second URL scraping
- Tried to set this up in a docker container and then export the container to AWS lambda using SAM
