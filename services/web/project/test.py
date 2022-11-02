from unicodedata import name
from dateutil.relativedelta import relativedelta
from datetime import datetime, date , time, timedelta
import requests
import urllib3
import json
import pandas as pd

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

params_movie = {
    'api_key': api_key,
    'primary_release_date.gte' : prmg ,
    'primary_release_date.lte' : prml ,  
    'page' : page
}

def movie_request(url_movie, params_movie):
    response = requests.get(url_movie, headers="", params=params_movie, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response
    else:
        response = json.loads(response.text, strict=False)
        return response["status_message"]

def get_pages(response):
    return response['total_pages']

def title_result(response):
    # title_result = []
    for item in response['results']:
        title_result = item['title']
        # title_result.append(char)
    return title_result

def genre_result(response):
    genre_id = []
    for item in response['results']:
        genres = item['id'],item['genre_ids']
        genre_id.append(genres)
    return genre_id


# 1 hónap múlva lévő idő
# datenow = date.today()
# datebefor = date.today() + relativedelta(months=-1)
# print (datenow)
# print (datebefor)


movie_data = movie_request(url_movie,params_movie)
for xyz in range (1,get_pages(movie_data)+1):
    pass
print(xyz)




# title_list= []
# data = main_request(url, params)
# for x in range (1,get_pages(data)+1):
#     print(x)
#     params['page']=x
#     title_list.extend(title_result(main_request(url, params)))
# print(title_list)
# print("title_listben szereplő adatok db száma")
# print(len(title_list))