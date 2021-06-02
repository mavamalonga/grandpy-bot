from flask import render_template, redirect, flash, jsonify, request
from app import app
from app.places import Places
from app.wiki import MediaWiki
from app.grandpy import Vocabulary

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
	if request.method == 'GET':
		voice = Vocabulary()
		catch_phrase =  voice.say()

	return render_template('index.html', catch_phrase=catch_phrase)

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):

	places = Places('AIzaSyAkDUNgcXqkdc5lEgcNf-DbetL0kDnkH-A', str(message))
	geolocation = places.get_geolocation()
	wiki = MediaWiki(str(message), geolocation)
	sentences = wiki.main()

	return jsonify({'geolocation': geolocation, 'sentences': sentences})
