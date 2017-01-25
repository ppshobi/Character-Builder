import json
from flask import Flask
from flask import render_template,url_for,redirect,request,make_response

from options import DEFAULTS

app=Flask(__name__)

@app.route('/')
def index():
	data=get_saved_data()
	return render_template("index.html",saves=data)

def get_saved_data():
	try:
		data=json.loads(request.cookies.get('character'))
	except TypeError:
		data={}
	return data

@app.route('/builder')
def builder():
	return render_template("builder.html",saves=get_saved_data(),options=DEFAULTS)

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('builder')))
	data=get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie('character',json.dumps(data))
	return response

app.run(debug=True, port=8000)