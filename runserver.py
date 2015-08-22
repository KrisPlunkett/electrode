#from flask import Flask
from flask import Flask, request, render_template

import logging
app = Flask(__name__)

# This is where we make our api endpoints

@app.route("/")
def home():
    return "Electrode. Powered by Python."

@app.route("/Andy")
def Andy():
	return render_template('index.html')

@app.route("/user/<username>")
def user(username):
    return "Hello user %s" % username

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4040, debug=True)
