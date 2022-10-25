from http.client import responses
from unicodedata import name
from urllib import response
from dateutil.relativedelta import relativedelta
from datetime import datetime, date , time, timedelta
import requests
import urllib3
import json
import pandas as pd
from . import db

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_genre = 'https://api.themoviedb.org/3/genre/movie/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'

params_api = {
    'api_key': api_key
}



def genre_request(url_genre, params_api ):
    response = requests.get(url_genre, headers="", params=params_api, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response
    else:
        response = json.loads(response.text, strict=False)
        return response["status_message"]

data = genre_request(url_genre, params_api )
print(data)


