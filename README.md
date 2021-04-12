# PostgreSQL management API
Flask + SQLAlchemy pet project
## Project features:

- Create&Delete Databases
- Create&Delete Schemas
- Create&Delete Tables
- Create&Delete Partitions

## How to run
Create .env file in the project directory or use any other way to store and use environment variables
1. Move to project directory:
   ```console
   user:~$ cd ../Postgres_Management_API
   ```

1. Install all roject requirements by command:
   ```
   pip install -r requirements.txt
   ```

1. Set up an environment variables:
   - Set up BASE_URL (The address your app is using):
    ```
   base_url = 'http://127.0.0.1:5000/'
    ```
   - Set up your PostrgeSQL connection variables:
   ```
   host = 'localhost'
   db_name = 'your_db_name'
   password = 'password'
    ```
2. Run app:
   ```console
   user:~$ python3 app.py
   ```