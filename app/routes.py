from flask import render_template, redirect, flash, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):
	jsonResponse = {
		'message': message, 
		'category': 'request',
		'status': 200
	}
	return  jsonify(jsonResponse)
