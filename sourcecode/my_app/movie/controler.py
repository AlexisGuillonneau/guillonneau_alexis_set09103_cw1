from werkzeug import abort
from flask import Blueprint
from flask import render_template, url_for, send_from_directory
import my_app.movie.model as bd
import my_app as app
import json
from random import shuffle



movie_blueprint = Blueprint('movie',__name__)
categories = sorted(bd.get_all_categories())
@movie_blueprint.route('/')
def index():
	res = bd.get_data_carousel()
	shuffle(res)
	return render_template('index.html',movies=res[:10], categories=categories),200

@movie_blueprint.route('/about')
def about():
	return render_template('about.html',categories=categories),200

@movie_blueprint.route('/report', methods=['POST'])
def report():
	return send_from_directory(directory='static/pdf',filename='report.pdf',as_attachment=True,attachment_filename='report.pdf')

@movie_blueprint.route('/category/<string:category>')
def category(category):
	res = bd.get_from_category(category)
	return render_template('category.html',movies=res[0],categories=categories,category=category),200

@movie_blueprint.route('/movies/<string:movie>')
def movie(movie):
	res = bd.get_movie(movie)
	return render_template('movie.html',movie=res,categories=categories),200

@movie_blueprint.route('/movies')
def display_all_movies():
	res = bd.get_all_data()
	actors = bd.get_all_actors()
	return render_template('all_movies.html',movies=res,categories=categories,actors=sorted(actors)),200

@movie_blueprint.route('/year/<int:year>')
def year(year):
	res = bd.get_all_data_for_year(year)
	return render_template('display_data.html',name="Movies in "+str(year),movies=res,categories=categories),200

@movie_blueprint.route('/actor/<string:actor>')
def actor(actor):
	print("yes")
	res = bd.get_all_data_for_actor(actor)
	return render_template('display_data.html',name="Movies where "+actor+" is starring",movies=res,categories=categories),200

@movie_blueprint.route('/country/<string:country>')
def country(country):
	res = bd.get_all_data_for_country(country)
	return render_template('display_data.html',name="Movies from "+country,movies=res,categories=categories),200

@movie_blueprint.route('/producer/<string:producer>')
def producer(producer):
	res = bd.get_all_data_from_producer(producer)
	return render_template('display_data.html',name="Movies produced by "+producer,movies=res,categories=categories),200

@movie_blueprint.route('/distribution/<string:distribution>')
def distribution(distribution):
	res = bd.get_all_data_from_distribution(distribution)
	return render_template('display_data.html',name="Movies distribued by "+distribution,movies=res,categories=categories),200

@movie_blueprint.route('/director/<string:director>')
def director(director):
	res = bd.get_all_data_from_director(director)
	return render_template('display_data.html',name="Movies leaded by "+director,movies=res,categories=categories),200

@movie_blueprint.app_errorhandler(404)
def error404(error):
	return render_template('error.html',categories=categories,error=error),404

@movie_blueprint.app_errorhandler(403)
def error403(error):
	return render_template('error.html',categories=categories,error=error),403
