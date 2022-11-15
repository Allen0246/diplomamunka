from http.client import responses
from unicodedata import name
from urllib import response
from dateutil.relativedelta import relativedelta
from datetime import datetime, date , time, timedelta
import requests
import urllib3
import json
import pandas as pd
from extensions.api import url_movie, params_movie

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_genre = 'https://api.themoviedb.org/3/genre/movie/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'

params_api = {
    'api_key': api_key
}





# data = genre_result1(url_genre, params_api )
# print(data)

responsee = requests.get(url_movie, headers="", params=params_movie, verify=False)
if  responsee.status_code == 200:
    responsee = json.loads(responsee.text, strict=False)
    for item in responsee['results']:
        title_result = item['title']
        print(title_result)


# def title_result(response):
#     # title_result = []
#     for item in response['results']:
#         title_result = item['title']
#         # title_result.append(char)
#     return title_result

def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()
 
print(increment(10))