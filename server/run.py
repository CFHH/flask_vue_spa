from flask import Flask, render_template
from random import *
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "../client/dist/static",
            template_folder = "../client/dist")
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/hello')
def hello():
    return "Hello, World !"

@app.route('/api/random')
def random_number():
    response = {
        'random_number': randint(1, 100)
    }
    return response

@app.route('/')
@app.route('/<path:path>')
def index():
    return render_template("index.html")