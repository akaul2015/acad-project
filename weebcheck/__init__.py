from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for

import os

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/home')
    def home():
        return render_template('home.html')
        #this is where the homepage/index will be of the site
    @app.route('/signup')
    def signup():
        return render_template('signup.html')
        #signup page


    @app.route('/')
    def homePg():
        return redirect(url_for('home'))
        #in case u go directly to website and dont enter anything in front of /

    return app
