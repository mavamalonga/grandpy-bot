from flask import render_template, redirect, flash, jsonify
from app import app
from app.forms import QuestionForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/<message>', methods=('GET', 'POST'))
def api(message):
	jsonResponse = {
		message: message, 
		category: "error",
		status: 404
	}
	return  jsonify(jsonResponse)
