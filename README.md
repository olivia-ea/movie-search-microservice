# Movie Search Microservice Challenge

## Table of Contents
* [Tasks](#tasks)
* [Tech Stack](#tech-stack)
* [Setting Up/Installation](#installation)
* [Files Explained](#files-explained)
* [Testing](#testing)
* [Personal](#personal)

## Tasks
Create a microservice that uses the OMDB API to do the following things:
* Search for movies using the exact movie title
* Conduct a movie search for movies with a partial movie title
* Conduct a movie search for movies with a partial movie title and year

## Tech Stack
* Backend: Python, Flask
* APIs: OMDB API

## Installation

To run the Movie Search microservice on your local computer, follow these steps:

Clone repository:
```
$ git clone https://github.com/olivia-ea/movie-search-microservice.git
```

Set up virtual environment:

```
$ virtualenv venv
```

Activate virtual envirnoment:
```
$ source venv/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Get OMBD API key from OMDB and save them to a file secrets.sh:
```
export MOVIE_API_KEY=YOUR_KEY
```

Run from the command line:
```
$ python3 server.py
```

Open localhost:5000 on browser.


## Files Explained
### server.py
* This file contains code only relating to the server.

### movieutils.py
* This file contains the all the endpoints for the movie search microservice.
* The functions hit the following endpoints:
    * /movies/<title>
    * /movies/search/<title>
    * /movies/search/?<title>&<year>
* When each endpoint is hit, a get request makes API call to the OMBD API. The return statement then parses through the json to give the desired format.

| URL      | HTTP Request Type     | Action     | Output     |
| :------------- | :---------- | :---------- | :----------- |
|  /movies/<title> | GET   | Given a movie title, this endpoint returns all the movie results with an exact title match.     | Returns the movie title, shortened plot summary, year released, runtime and genre.   |
|  /movies/search/<title> | GET   | Given a partial movie title, this endpoint returns all the movie results with a partial title match.    | Returns the movie title and year released.    |
|  /movies/search/?<title>&<year> | GET   | Given a partial movie title and year, this endpoint returns all the movie results with a partial title match and exact year match.     | Returns the movie title and year released.    \|

### testing.py
* Contains unit testing for above files. There is an individual function to test each endpoint using assert statements. The valid id tests are checking for a 200 status code and if a response is present whereas the invalid id tests are checking for a 500 status code.


## Testing

In order to run the unit tests in the testing.py file, first run server.py and then the nosetest.

```
$ python3 server.py
```

```
$ nosetests --verbosity=2 testing.py
```

## Personal

### Major challenges
IN PROGRESS

### New things I learned:
IN PROGRESS

### Future enhancements:
IN PROGRESS

