from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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

        if len(email) < 4:
            flash('email must be greater than 3 characters', category='ERROR')
        elif len(firstName) < 2:
            flash('firstName must be greater than 1 characters', category='ERROR')
        elif password1 != password2:
            flash('passwords don\'t match', category='ERROR')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters', category='ERROR')
        else:
            #add user to database
            flash('Account created', category='SUCCESS')

    return render_template('signup.html')