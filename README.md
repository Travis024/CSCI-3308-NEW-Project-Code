# CSCI-3308-Team-101-3-Project-Code

Python(3.7.2)
PostgreSQL(11.2)
Psycopg2(2.7.7)- Python adapter for Postgres
Flask-SQLAlchemy(2.1)- Flask extension that provides SQLAlchemy support
Flask-Migrate(1.8.0)- Extension that supports SQLAlchemy database migrations


Install virtualenv (Virtual Python Enviornment)
1. $ pip install virtualenv
2. cd into project director
3. $ virtualenv venv
4. Now you have a virtual environment set up in project (Note: the virtual enviornment needs to be created in the smae directory where you app files are located)

Activating the virtual environment
1. Make sure you are in the project directory
2. For Mac/Linux: $ . venv/bin/activate
3. For Windows: venv/Scripts/activate
4. Close Virtual environment: $deactivate

Installing Flask
1. activate virtual enviornment
2. $ pip install flask

Install other dependencies
1. pip install psycopg2
2. pip install Flask-SQLAlchemy===2.1
3. pip install Flask-Migrate==1.8.0
