# Source: https://medium.com/analytics-vidhya/flask-restful-api-with-heroku-da1ecf3e04b

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

class status(Resource):
    def get(self):
        try:
            return {'data': 'API is running'}
        except:
            return {'data': 'Error'}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})

api.add_resource(status,'/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()