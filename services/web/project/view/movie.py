from turtle import title
from flask import Blueprint
from requests import request
from ..extensions.api import params,main_request,genre_result,title_result, url, get_pages

movie = Blueprint('movie', __name__)


@movie.route('/movie' , methods=['GET'])
def movie():
    if request.method == 'GET':
        
        title_list= []
        data = main_request(url, params)
        for x in range (1,get_pages(data)+1):
            params['page']=x
        title_list.extend(title_result(main_request(url, params)))
        
        genre_list= []
        data = main_request(url, params)
        for x in range (1,get_pages(data)+1):
            params['page']=x
        genre_list.extend(genre_result(main_request(url, params)))



    db.session.add(genres_id)
    db.session.add(title)
    db.session.commit()