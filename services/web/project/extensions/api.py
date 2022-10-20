import requests
import urllib3
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_movie = 'https://api.themoviedb.org/3/discover/movie'
url_genre = 'https://api.themoviedb.org/3/genre/moviee/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'
years = ['2015', '2016']

prmg = ['2022-09-30']
# prmg = ['1975-01-01']
prml = ['2022-09-30']
page = 1
params_api = {
    'api_key': api_key
}
params = {
    'api_key': api_key,
    'primary_release_date.gte' : prmg ,
    'primary_release_date.lte' : prml ,  
    'page' : page
}

def genre_request(url_genre, params_api ):
    response = requests.get(url_genre, headers="", params=params_api, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response
    else:
        response = json.loads(response.text, strict=False)
        return response["status_message"]

def main_request(url_movie, params):
    response = requests.get(url_movie, headers="", params=params, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response

def get_pages(response):
    return response['total_pages']

def title_result(response):
    title_result = []
    for item in response['results']:
        char = item['title']
        title_result.append(char)
    return title_result

def genre_result(response):
    genre_id = []
    for item in response['results']:
        char = item['genre_ids']
        genre_id.append(char)
    return genre_id