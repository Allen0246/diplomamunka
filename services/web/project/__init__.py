from flask import Flask, render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
from .extensions.api import genre_request , url_genre , params_api

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



data = genre_request(url_genre,params_api)
if type(data) != str:
    for r in data['genres']:
        genres = Genre(r['id'], r['name'] )
        db.session.add(genres)
        db.session.commit()
else:
    log_system.error = data()


#logolni a hibát.

# Genre táblába adatfelvitel
# kategoria = Genre('')
# db.session.add(kategoria)
# db.session.commit()



# Action =Genre(genre_id = '28' , genre = 'Action')
# Adventure = Genre(genre_id = '12' , genre = 'Adventure')
# Animation = Genre(genre_id = '16' , genre = 'Animation')
# Comedy = Genre(genre_id = '35' , genre = 'Comedy')
# Crime = Genre(genre_id = '80' , genre = 'Crime')
# Documentary = Genre(genre_id = '99' , genre = 'Documentary')
# Drama = Genre(genre_id = '18' , genre = 'Drama')
# Family = Genre(genre_id = '10751' , genre = 'Family')
# Fantasy = Genre(genre_id = '14' , genre = 'Fantasy')
# History = Genre(genre_id = '36' , genre = 'History')
# Horror = Genre(genre_id = '27' , genre = 'Horror')
# Music = Genre(genre_id = '10402' , genre = 'Music')
# Mystery = Genre(genre_id = '9648' , genre = 'Mystery')
# Romance = Genre(genre_id = '10749' , genre = 'Romance')
# Science_Fiction = Genre(genre_id = '878' , genre = 'Science Fiction')
# TV_Movie = Genre(genre_id = '10770' , genre = 'TV Movie')
# Thriller = Genre(genre_id = '53' , genre = 'Thriller')
# War = Genre(genre_id = '10752' , genre = 'War')
# Western = Genre(genre_id = '37' , genre = 'Western')

# db.session.add(Action,Adventure,Animation)
# db.session.add(Comedy,Crime,Documentary)
# db.session.add(Drama,Family,Fantasy)
# db.session.add(History,Horror,Music)
# db.session.add(Mystery,Romance,Science_Fiction)
# db.session.add(TV_Movie,Thriller,War,Western)
# db.session.commit()


# # THREADS


