from cmath import log
from flask import Flask, render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
import requests
import urllib3
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_movie = 'https://api.themoviedb.org/3/discover/movie'
url_genre = 'https://api.themoviedb.org/3/genre/movie/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'
years = ['2015', '2016']

prmg = ['2022-09-30']
# prmg = ['1975-01-01']
prml = ['2022-09-30']
page = 1
params_api = {
    'api_key': api_key
}
params_movie = {
    'api_key': api_key,
    'primary_release_date.gte' : prmg ,
    'primary_release_date.lte' : prml ,  
    'page' : page
}



# def movie_request(url_movie, params_movie):
#     response = requests.get(url_movie, headers="", params=params_movie, verify=False)
#     if  response.status_code == 200:
#         response = json.loads(response.text, strict=False)
#     return response

# movie_data= movie_request(url_movie,params_movie)
# print(movie_data)


def movie_request(url_movie, params_movie):
    response = requests.get(url_movie, headers="", params=params_movie, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        response_tuple = ()
        for page in range(1, response.get('total_pages') + 1):
            params_movie['page']=page
            response= requests.get(url_movie, headers="", params=params_movie, verify=False)
            if  response.status_code == 200:
                response = json.loads(response.text, strict=False)
            response_tuple = list(response_tuple)
            response_tuple.append(response)
            response_tuple = tuple(response_tuple)
        return response_tuple
    else:
        response = json.loads(response.text, strict=False)
        return response["status_message"]
        
movie_data= movie_request(url_movie,params_movie)
print(movie_data)

# for response in movie_data.get('results'):
#     print(id = response.get('id'))
#     title = response.get('title')
#     genre_ids = response.get('genre_ids')