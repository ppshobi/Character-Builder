import json
from flask import Flask
from flask import render_template,url_for,redirect,request,make_response

app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('index')))
	response.set_cookie('character',json.dumps(dict(request.form.items())))
	return response

app.run(debug=True, port=8000)