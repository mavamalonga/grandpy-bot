from flask import render_template, redirect, flash, jsonify
from app import app
from app.bot_words import Dictionary_Of_Words
from app.places import Places
from app.wiki import MediaWiki

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):

	places = Places('AIzaSyAkDUNgcXqkdc5lEgcNf-DbetL0kDnkH-A', str(message))
	geolocation = places.get_geolocation()
	wiki = MediaWiki(str(message), geolocation)
	sentences = wiki.main()

	return jsonify({'geolocation': geolocation, 'sentences': sentences})
