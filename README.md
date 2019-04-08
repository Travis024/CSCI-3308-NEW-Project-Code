# livBoulderPostgres
Requirements
1. Python(3.7.2)
2. PostgreSQL(11.2)
3. Psycopg2(2.7.7)- Python adapter for Postgres
3. Flask-SQLAlchemy(2.3.2)- Flask extension that provides SQLAlchemy support
4. SQLAlchemy(1.3.2)
5. Flask-Migrate(1.8.0)- Extension that supports SQLAlchemy database migrations


Install virtualenv (Virtual Python Enviornment)
1. $ ```pip install virtualenv```
2. cd into project director
3. $ ```virtualenv venv```
4. Now you have a virtual environment set up in project (Note: the virtual enviornment needs to be created in the smae directory where you app files are located)

Activating the virtual environment
1. Make sure you are in the project directory
2. For Mac/Linux: ```$ . venv/bin/activate```
3. For Windows: ```venv/Scripts/activate```
4. Close Virtual environment: ```deactivate```

Install other dependencies
1. Cd into directory
2. activate your virtualenv.
3. run: ```pip install -r requirements.txt``` in your shell.

Setup Database Locally **** DO THIS BEFORE RUNNING ***
1. cd into project directory
2. create a file .flaskenv
3. Paste
```
  FLASK_APP=livBoulder.py
  APP_SETTINGS="config.DevelopmentConfig"
  DATABASE_URL="postgresql+psycopg2://user:password@localhost:5432/nameOfDatabase"
```
4. REMEMBER YOU NEED TO CONFIGURE A POSTGRES DATABASE LOCALLY FOR THIS TO WORK
5. You will need to input your parameters to you local postgres db into the DATABASE_URL above given that:
    user = your local db user
    password = password associated with that user
    nameOfDatabase = the name you gave to the database
6. with venv running run: ```flask db init``` in your shell.
7. then run: ```flask db migrate```
8. then run: ```flask db upgrade```
9. Now your local postgres db should be set up with the app

To RUN app
1. make sure your virtualenv is running
2. run: ```flask run```

Resources
1. Problems with installing psycopg2 on mac
    https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl
2. Using postgres through SQLAlchemy
    https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
3. Database migrations
    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
