from flask import Flask
from flask_restful import Api, Resource
from tests import test_endpoint

app = Flask(__name__)
api = Api(app)


class HeyMike(Resource):
    def get(self):
        return 'Hey, Mike))'


api.add_resource(HeyMike, 'hey')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    test_endpoint('hey')
