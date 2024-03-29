from flask import Blueprint, render_template, request, flash
import sys
sys.path.append('./SnakeMap')
import agent

def StartSnake():
    return agent.train()


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "test"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) <2:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')
            pass


    return render_template("sign_up.html")

@auth.route('/snake', methods = ['GET', 'POST'])

def snake():
    return render_template("reinforcement_snake.html", StartSnake = StartSnake)

def upload_file():
   return render_template('upload.html')
	
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'
    