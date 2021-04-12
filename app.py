from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from constants import YOUR_POSTGRES
import sqlalchemy

from tests import test_post_endpoint

app = Flask(__name__)
api = Api(app)
engine = sqlalchemy.create_engine(YOUR_POSTGRES)


# app.config['SQLALCHEMY_DATABASE_URI'] = YOUR_POSTGRES

db = SQLAlchemy(app)


class HeyMike(Resource):

    def get(self):
        return {'message': 'Hey, Mike))'}


class DataBases(Resource):

    def get_databases(self):
        return engine.execute('SELECT datname FROM pg_database;').fetchall()

    def create_database(self, database_name):
        conn = engine.connect()
        conn.execute('commit')
        conn.execute(f"create database {database_name}")
        conn.close()
        return {'message': f'database {database_name} is created'}


api.add_resource(HeyMike, '/hey')
api.add_resource(DataBases, '/get_db')
api.add_resource(DataBases, '/create_db/<string:database_name>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    test_post_endpoint('create_db/test')