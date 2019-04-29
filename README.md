# livBoulderPostgres

## About

This is the project code for Team 101-3 in CSCI 3308. Over the course of the semester we put our newly learned skills to use as we built a Boulder-based activity recommendation web application named LivBoulder.

Boulder, Colorado is a place with adventures and activities for everybody, but that doesn’t mean that finding the perfect thing to do on a gorgeous Colorado day is easy! Making choices can often be rather difficult, and residents of Boulder end up spending more time on the internet looking up what to do than actually getting outside and enjoying mother nature!

LivBoulder, an online outdoor activity finding website, seeks to combat this exact problem. Shortly after signing up, users will be given the opportunity to fill out their preferences for outdoor activities including length of activity, difficulty of activity, season for activity, and more. Our website will then pull suggestions from a database that are personalized for users based on their preferences, thus eliminating the constant Googling required to find something to do elsewise.

## Organization

The folder "app" contains a folder for all of the templates for our HTML pages. Further, it contains the folder "static", which contains an image folder, a CSS folder, and a folder for all JavaScript files.

The folder "Databases" contains some of our database mock-ups, though actual database activity when the app is running is handled by Flask, found within the "\__pycache__" and "migrations" folders.

"TEST CASES" contains all of the test cases that were run to test the application.

## Running the Application

### Requirements
1. Python(3.7.2)
2. PostgreSQL(11.2)
3. Psycopg2(2.7.7)- Python adapter for Postgres
3. Flask-SQLAlchemy(2.3.2)- Flask extension that provides SQLAlchemy support
4. SQLAlchemy(1.3.2)
5. Flask-Migrate(1.8.0)- Extension that supports SQLAlchemy database migrations


### Install virtualenv (Virtual Python Enviornment)
1. $ ```pip install virtualenv```
2. cd into project director
3. $ ```virtualenv venv```
4. Now you have a virtual environment set up in project (Note: the virtual enviornment needs to be created in the smae directory where you app files are located)

### Activating the virtual environment
1. Make sure you are in the project directory
2. For Mac/Linux: ```$ . venv/bin/activate```
3. For Windows: ```venv/Scripts/activate```
4. Close Virtual environment: ```deactivate```

### Install other dependencies
1. Cd into directory
2. activate your virtualenv.
3. run: ```pip install -r requirements.txt``` in your shell.

### Setup Database Locally ** DO THIS BEFORE RUNNING **
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

### To RUN app
1. make sure your virtualenv is running
2. run: ```flask run```

### Resources
1. Problems with installing psycopg2 on mac
    https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl
2. Using postgres through SQLAlchemy
    https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
3. Database migrations
    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
