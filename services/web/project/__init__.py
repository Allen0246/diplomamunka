from cmath import log
from flask import Flask, render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
from .extensions.api import genre_request , url_genre , params_api, movie_request, url_movie, params_movie, get_pages, title_result, genre_result ,movieid_result

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('project.config.default')

db = SQLAlchemy(app)
    
#LOGGING
from .extensions.logging import create_log_file

# CREATE SYSTEM LOG
log_system = create_log_file('MOOVIE_RECOMMENDATION_LOG')
log_system.info('Start...')

#LOGINMANAGER
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'A megtekintéshez lépjen be!'
login_manager.refresh_view = 'auth.login'
login_manager.needs_refresh_message = 'Lépjen be újra!'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    


# MODEL
from .model.user import User
from .model.movie import Movie
from .model.genre import Genre

# CREATE TABLES
db.create_all()
db.session.commit()

# VIEW/BLUEPRINT
from .view.auth import auth
app.register_blueprint(auth)

# LOG OUT AFTER 100 MINUTES
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=100)

# 404 MESSAGE
@app.errorhandler(404)
def page_not_found(e):
    flash('code: 404, title: Page not found.','danger')
    return redirect(url_for('index'))

# GENERAL ERROR HANDLER
@app.errorhandler(Exception)
def handle_exception(e):
    flash('EZT HASZNÁLJA:{}'.format(e),'danger')
    return redirect(url_for('index'))

# MAIN ROUTE
@app.route('/')
def index():
    return render_template('home.html')


# Genre adatt felvitel
log_system.info('Genre adatfelvitel megkezdése ...')
genre_data = genre_request(url_genre,params_api)
if type(genre_data) != str:
    for r in genre_data['genres']:
        genre_db = Genre.query.filter_by(genre=r['name']).first()
        if not genre_db:
            genres = Genre(r['id'], r['name'] )
            db.session.add(genres)
            db.session.commit()
            log_system.info('Sikeresen hozzá let adva a követekző műfaj: {0}'.format(r['name']))
        else:
            log_system.info('Már szerepel az adatbázisban: {0}'.format(r['name']))
else:
    log_system.error('Az alábbi miatt nem sikerült felvinni a műfaj adatokat: {0}'.format(genre_data))

log_system.info('Movie adatfelvitel megkezdése ...')
movie_data = movie_request(url_movie, params_movie)
if type(movie_data) != str:
    for movie_results in movie_data:
        movie_db = Movie.query.filter_by(title=movie_results['title']).first()
        if not movie_db:
            for response in movie_data.get('results', list()):
                id = response.get('id')
                title = response.get('title')
                genre_ids = response.get('genre_ids')
                movie = Movie(id, title)
                db.session.commit()
                log_system.info('Sikeresen hozzá lettek adva a műfaj id-k és film címek.')
else:
    log_system.error('Az alábbi miatt nem sikerült felvinni a film és műfaj id-ket: {0}'.format(movie_data))


# THREADS


