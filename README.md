# livBoulderPostgres
Requirements
1. Python(3.7.2)
2. PostgreSQL(11.2)
3. Psycopg2(2.7.7)- Python adapter for Postgres
3. Flask-SQLAlchemy(2.3.2)- Flask extension that provides SQLAlchemy support
4. SQLAlchemy(1.3.2)
5. Flask-Migrate(1.8.0)- Extension that supports SQLAlchemy database migrations


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
1. Cd into directory
2. activate your virtualenv.
3. run: pip install -r requirements.txt in your shell.


Resources
1. Problems with installing psycopg2 on mac
    https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl
2. Using postgres through SQLAlchemy
    https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
3. Database migrations
    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
