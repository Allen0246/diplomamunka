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

def get_pages(response):
    return response['total_pages']


def title_result(response):
    for item in response['results']:
        title_result = item['title']
    return title_result

def genre_result(response):
    for item in response['results']:
            list_int = item['genre_ids']
            list_string = map(str, list_int)
            genre_id=(', '.join(list(list_string)))
    return genre_id


def movie_request(url_movie, params_movie):
    response = requests.get(url_movie, headers="", params=params_movie, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)
        return response
    else:
        response = json.loads(response.text, strict=False)
        return response["status_message"]

def title_result(response):
    for item in response['results']:
        title_result = item['title']
    return title_result


# def test():
#     data = ['egy','kettő','három']
#     for item in data:
#         data2 = item[0]
#         return data2

# print(test())

# data = movie_request(url_movie, params_movie)
# data2 =genre_result(data)
# data3 = title_result(data)
# print(data2)


# print(data['results'][0]['title'])
# for item in data['results']:
#     list_int = item['genre_ids']
#     list_string = map(str, list_int)
#     print(', '.join(list(list_string)))

# s = ''.join(str(x) for x in data2)
# print(s)
names = ["Sam", "Peter", "James", "Julian", "Ann"]
for n in names:
    # print(number)
    number = ['1' , '2', '3']
    for item in number:
        print(item)
        print(n)
# print(', '.join(names))


# print(data3)

# print (data['results'][0]['title'])
# print(title_result(url_movie, params_movie))

# l = ['01', '1.0', '[0.2]']
# valami = [i.strip('[]') for i in l]
# print(valami)


def title_result(response):
    result = list()
    for item in response['results']:
        result.append(item['title'])
        title_result = item['title']
    return result