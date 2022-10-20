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

url = 'https://api.themoviedb.org/3/discover/movie'
url_genre = 'https://api.themoviedb.org/3/genre/movie/list'
api_key = 'a151c76b6aad5c4efbeac150479b0718'
years = ['2015', '2016']

prmg = ['2022-09-30']
# prmg = ['1975-01-01']
prml = ['2022-09-30']
page = 1

params = {
    'api_key': api_key,
    'primary_release_date.gte' : prmg ,
    'primary_release_date.lte' : prml ,  
    'page' : page
}

def main_request(url, params):
    response = requests.get(url, headers="", params=params, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response

def get_pages(response):
    return response['total_pages']

def title_result(response):
    title_result = []
    for item in response['results']:
        titles = item['id'],item['title']
        title_result.append(titles)
    return title_result

def genre_result(response):
    genre_id = []
    for item in response['results']:
        genres = item['id'],item['genre_ids']
        genre_id.append(genres)
    return genre_id

# title_list= []
# data = main_request(url, params)
# for x in range (1,get_pages(data)+1):
#     print(x)
#     params['page']=x
#     title_list.extend(title_result(main_request(url, params)))
# print(title_list)
# print("title_listben szereplő adatok db száma")
# print(len(title_list))

genre_list= []
data = main_request(url, params)
for x in range (1,get_pages(data)+1):
    print(x)
    params['page']=x
    genre_list.extend(title_result(main_request(url, params)))
print(genre_list)
print("genre_listben szereplő adatok db száma")
print(len(genre_list))


df = pd.DataFrame(genre_list)

df.to_csv('charlist.csv' , index = False, header=None)


# 1 hónap múlva lévő idő
datenow = date.today()
datebefor = date.today() + relativedelta(months=-1)
print (datenow)
print (datebefor)
