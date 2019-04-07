from flask import Flask, render_template, request, redirect, url_for
from models import db

app = Flask(__name__)

# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'password',
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': '5432',
# }
#
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")
# def home():
#     if 'username' in session:
#         return 'Logged in as %s'
#     return 'Please Login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run()
