import os
import psycopg2

connection_string = f"host='{os.getenv('host')}' dbname='{os.getenv('db_name')}' user='postgres' password='{'password'}'"


BASE_URL = os.getenv('base_url') + '{endpoint_name}'
YOUR_POSTGRES = psycopg2.connect(connection_string)
