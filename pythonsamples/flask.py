#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to Python"

if __name__ == '__main__':
	app.run(host='localhost')