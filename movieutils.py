from flask import Flask, request
import requests
import os

MOVIE_API_KEY = os.environ['MOVIE_API_KEY']
BASE_URL = 'http://www.omdbapi.com/?'

app = Flask(__name__)
app.debug = True

# http://localhost:5000/movies/jurassic+park
@app.route('/movies/<title>', methods=['GET'])
def fetch_movies_using_exact_title_search(title):
    api_call_url = BASE_URL + "t=" + title + "&type=movie&plot=short&apikey=" + MOVIE_API_KEY
    response_data = requests.get(api_call_url)
    json_data = response_data.json()
    movie_response = {}
    if json_data["Response"] == "True":
        movie_response["title"] = json_data["Title"]
        movie_response["short_plot"] = json_data["Plot"]
        movie_response["year_released"] = json_data["Year"]
        movie_response["run_time"] = json_data["Runtime"]
        movie_response["genre"] = json_data["Genre"]
        return movie_response, 200
    else:
        movie_response["Error"] = json_data["Error"]
        return movie_response, 500

# http://localhost:5000/movies/search/jurassic+park
@app.route('/movies/search/<title>', methods=['GET'])
def fetch_all_movies_by_title(title):
    api_call_url = BASE_URL + "s=" + title + "&type=movie&apikey=" + MOVIE_API_KEY
    response_data = requests.get(api_call_url)
    json_data = response_data.json()

    # TODO for testing check if array length is > 0

    if json_data["Response"] == "True":
        movie_results = {'Results': []}
        for movie in json_data['Search']:
            movie_response = {}
            movie_response["title"] = movie["Title"]
            movie_response["year_released"] = movie["Year"]
            movie_results['Results'].append(movie_response)
        return movie_results, 200
    else:
        movie_response = {}
        movie_response["Error"] = json_data["Error"]
        return movie_response, 500

# http://localhost:5000/movies/search/?title=jurassic+park&year=1993
@app.route('/movies/search/', methods=['GET'])
def fetch_all_movies_by_title_and_year():
    title = request.args.get('title')
    title = title.replace(" ", "+")
    year = request.args.get('year')
    api_call_url = BASE_URL + "s=" + title + "&y=" + year + "&type=movie&apikey=" + MOVIE_API_KEY
    response_data = requests.get(api_call_url)
    json_data = response_data.json()

    if json_data["Response"] == "True":
        movie_results = {'Results': []}
        for movie in json_data['Search']:
            movie_response = {}
            movie_response["title"] = movie["Title"]
            movie_response["year_released"] = movie["Year"]
            movie_results['Results'].append(movie_response)
        return movie_results, 200
    else:
        movie_response = {}
        movie_response["Error"] = json_data["Error"]
        return movie_response, 500

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

# TODO:
# exact title => /movies/exact/ =>fetch plot info (short), year released, run time, genre
# search movie => /movies/ list of search results
# search movie + year => give results for year
# cannot seach JUST BY year => needs to have movie title AND year



