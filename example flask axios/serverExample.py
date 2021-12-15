import flask
from flask import Flask, request, render_template, Blueprint  # pip install flask
import time
# this is the server. it will listen for the request from the website (the js and html file) which you'll see on website

# creates a flask "app". everything server related will be attached to this app. __name__ is the name of the python file
app = Flask(__name__)


@app.route('/')
# this is a decorator. it changes the behavior of a function. its not that important tbh, it just means that when the js asks this servr for the / endpoint, whatever function bellow
# an endpoint is a page or section of a website. it allows for example www.example.com/login vs www.example.com/homepage
def index():

    return render_template('index.html')


# the methods, it wont let methods not listed in the methods array to to the function bellow
@app.route('/login', methods=['GET', 'POST'])
# for this endpoint it will accept both a get for the webpage
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:  # use POST here so the username and password dont go in the url bar. that would be bad
        # you'd do something meaningful with this
        print(request.form.get('username'), request.form.get('password'))
        return flask.redirect('/loggedin')


@app.route('/loggedin')
def loggedin():
    return render_template('home.html')


@app.route('/getTime')
def getTime():
    return str(time.time())


app.run(debug=True)  # debug means that the app will reload when we change this file. it will also display error messages when something is wrong on the webpage
