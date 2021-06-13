from flask import render_template, redirect, flash, jsonify, request
from app import app
from app.places import Places
from app.wiki import MediaWiki
from app.grandpy import Brain
from app.parse_question import Parse

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
	brain = Brain()
	grandpy_say = brain.main()
	return render_template('index.html', say=grandpy_say['phrase'], time=grandpy_say['time'])

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):
	parse = Parse(message)
	parsed_message = parse.main()
	wiki = MediaWiki(parsed_message)
	text = wiki.main()
	return jsonify({'geo': 'location', 'text': text})

