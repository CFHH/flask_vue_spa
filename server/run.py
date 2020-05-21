from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restful import Resource, Api
from random import *


app = Flask(__name__,
            static_folder = "../client/dist/static",
            template_folder = "../client/dist")
cors = CORS(app, resources={"/api/*": {"origins": "*"}})
api = Api(app)


class DataSourceResource(Resource):
    def get(self, data_source_id):
        return {"method": "get", "object_id": data_source_id, "object_type": "datasource"}

    def post(self, data_source_id):
        data = request.get_json(True)
        return {"method": "post", "object_id": data_source_id, "object_type": "datasource", "data": data}

    def delete(self, data_source_id):
        return {"method": "delete", "object_id": data_source_id, "object_type": "datasource"}

api.add_resource(
    DataSourceResource, "/api/data_sources/<data_source_id>", endpoint="data_source"
)


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