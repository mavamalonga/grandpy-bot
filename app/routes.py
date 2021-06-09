from flask import render_template, redirect, flash, jsonify, request
from app import app
from app.places import Places
from app.wiki import MediaWiki
from app.grandpy import Vocabulary
from app.parse_question import Parse

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
	return render_template('index.html')

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):
	parse = Parse(message)
	parsed_message = parse.main()
	print(parsed_message)
	wiki = MediaWiki(parsed_message)
	text = wiki.main()

	return jsonify({'geo': 'location', 'text': text})
