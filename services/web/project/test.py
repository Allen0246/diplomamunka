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
params_genre = {
    'api_key': api_key
}
params = {
    'api_key': api_key,
    'primary_release_date.gte' : prmg ,
    'primary_release_date.lte' : prml ,  
    'page' : page
}
def genre_request(url_genre, params_genre):
    response = requests.get(url_genre, headers="", params_genre=params_genre, verify=False)
    if  response.status_code == 200:
        response = json.loads(response.text, strict=False)

def genreid(response):
    genreid= []
    for genre in response['genres']:
        print(genre['name'],genre['id'])
        genres = genre['name']
        genreid.append(genres)
    return genreid

data_genre= genre_request(url_genre, params_genre)
genreid(data_genre)


def genrename(response):
    genrename= []
    for genre in response['genres']:
        genres = genre['name']
        genrename.append(genres)
    return genrename



# def main_request(url, params):
#     response = requests.get(url, headers="", params=params, verify=False)
#     if  response.status_code == 200:
#         response = json.loads(response.text, strict=False)
#         return response

# def get_pages(response):
#     return response['total_pages']

# def title_result(response):
#     title_result = []
#     for item in response['results']:
#         titles = item['id'],item['title']
#         title_result.append(titles)
#     return title_result

# def genre_result(response):
#     genre_id = []
#     for item in response['results']:
#         genres = item['id'],item['genre_ids']
#         genre_id.append(genres)
#     return genre_id

# # title_list= []
# # data = main_request(url, params)
# # for x in range (1,get_pages(data)+1):
# #     print(x)
# #     params['page']=x
# #     title_list.extend(title_result(main_request(url, params)))
# # print(title_list)
# # print("title_listben szereplő adatok db száma")
# # print(len(title_list))

# genre_list= []
# data = main_request(url, params)
# for x in range (1,get_pages(data)+1):
#     print(x)
#     params['page']=x
#     genre_list.extend(title_result(main_request(url, params)))
# print(genre_list)
# print("genre_listben szereplő adatok db száma")
# print(len(genre_list))


# df = pd.DataFrame(genre_list)

# df.to_csv('charlist.csv' , index = False, header=None)


# # 1 hónap múlva lévő idő
# datenow = date.today()
# datebefor = date.today() + relativedelta(months=-1)
# print (datenow)
# print (datebefor)

# # Action =Genre(genre_id = '28' , genre = 'Action')
# # Adventure = Genre(genre_id = '12' , genre = 'Adventure')
# # Animation = Genre(genre_id = '16' , genre = 'Animation')
# # Comedy = Genre(genre_id = '35' , genre = 'Comedy')
# # Crime = Genre(genre_id = '80' , genre = 'Crime')
# # Documentary = Genre(genre_id = '99' , genre = 'Documentary')
# # Drama = Genre(genre_id = '18' , genre = 'Drama')
# # Family = Genre(genre_id = '10751' , genre = 'Family')
# # Fantasy = Genre(genre_id = '14' , genre = 'Fantasy')
# # History = Genre(genre_id = '36' , genre = 'History')
# # Horror = Genre(genre_id = '27' , genre = 'Horror')
# # Music = Genre(genre_id = '10402' , genre = 'Music')
# # Mystery = Genre(genre_id = '9648' , genre = 'Mystery')
# # Romance = Genre(genre_id = '10749' , genre = 'Romance')
# # Science_Fiction = Genre(genre_id = '878' , genre = 'Science Fiction')
# # TV_Movie = Genre(genre_id = '10770' , genre = 'TV Movie')
# # Thriller = Genre(genre_id = '53' , genre = 'Thriller')
# # War = Genre(genre_id = '10752' , genre = 'War')
# # Western = Genre(genre_id = '37' , genre = 'Western')
# # db.session.add(Action,Adventure,Animation,Comedy,Crime,Documentary,Drama,Family,Fantasy,History,Horror,Music,Mystery,Romance,Science_Fiction,TV_Movie,Thriller,War,Western)
# # db.session.commit()

# # genre id-k
# # 28 = Action
# # 12 = Adventure
# # 16 = Animation
# # 35 = Comedy
# # 80 = Crime
# # 99 = Documentary
# # 18 = Drama
# # 10751 = Family
# # 14 = Fantasy
# # 36 =  History
# # 27 =  Horror
# # 10402 = Music
# # 9648 = Mystery
# # 10749 = Romance
# # 878 = Science Fiction
# # 10770 = TV Movie
# # 53 = Thriller
# # 10752 = War
# # 37 = Western
