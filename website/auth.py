from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully.', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='ERROR')
        else:
            flash('Email does not exist.', category='ERROR')

    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='ERROR')

        elif len(email) < 4:
            flash('email must be greater than 3 characters', category='ERROR')
        elif len(firstName) < 2:
            flash('firstName must be greater than 1 characters', category='ERROR')
        elif password1 != password2:
            flash('passwords don\'t match', category='ERROR')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters', category='ERROR')
        else:
            #add user to database
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='SUCCESS')
            return redirect(url_for('views.home'))

    return render_template('signup.html')