import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

info = {
    'i1': {'title': 'the boys'},
    'i2': {'title': 'test titles'}
}

class TestRes(Resource):
    
    def get(self):
        # return "Test!!!"
        # print(f"info id is: {infoId}")
        # if infoId == "all":
        return jsonify(info)
        # return jsonify(info[infoId])

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        print("hello")
        pass

    # a simple page that says hello
    # @app.route('/hello')
    # @app.route('/')
    # def hello():
    #     return '<h1>Hello, World!<h1>'

    api.add_resource(TestRes, '/')
    # api.add_resource(TestRes, '/<infoId>')

    return app

# run on 8080