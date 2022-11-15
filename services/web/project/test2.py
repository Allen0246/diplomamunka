from http.client import responses
from unicodedata import name
from urllib import response
from dateutil.relativedelta import relativedelta
from datetime import datetime, date , time, timedelta
import requests
import urllib3
import json
import pandas as pd
from project import movie_request,url_movie,params_movie
from .model.movie import Movie
from . import db

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_genre = 'https://api.themoviedb.org/3/genre/movie/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'

params_api = {
    'api_key': api_key
}


movie_data = movie_request(url_movie, params_movie)
if type(movie_data) != str:
    for r in movie_data['results']:
        print (r)
        # movie_db = Movie.query.filter_by(movie_data['title']).first()
        # if not movie_db:
        #     for x in range (1,get_pages(movie_data)+1):
        #         params_movie['page']=x
        #         title_list = (title_result1(url_movie, params_movie))
        #         genre_id = (genre_result1(url_movie, params_movie))
        #         movie_result = Movie(title_list,genre_id)
        #         db.session.add(movie_result)
        #         db.session.commit()

