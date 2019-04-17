from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, g, json
from app.models import User
from flask_login import logout_user, login_user, current_user, login_required


@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template("homePostLogin.html")
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None:
        flash('Username is invalid', 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash('Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    return redirect(url_for('home'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/quiz", methods=['GET'])
@login_required
def quiz():
    return render_template("quiz.html")



@app.route("/returner", methods=['POST'])
@login_required
def returner():
    data = request.get_json()
    data = data['numYes']
    user = User.query.filter_by(username=current_user.username).first()
    user.recommendScore = data
    db.session.commit()
    return '', 200


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        user = User(request.form['firstName'],
                    request.form['lastName'],
                    request.form['email'],
                    request.form['username'],
                    request.form['password'],
                    0)
        isUsernameValid = User.query.filter_by(username=request.form['username']).first()
        if isUsernameValid is None:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('quiz'))
        flash('Username is being used', 'error')
        return redirect(url_for('register'))

@app.before_request
def before_request():
    g.user = current_user
