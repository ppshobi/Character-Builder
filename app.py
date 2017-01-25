from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/save', methods=['POST'])
def save():
	return "Saved"

app.run(debug=True, port=8000)