from flask import Blueprint, render_template
import sys
sys.path.append('./SnakeMap')
import agent


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", test = agent.train())

@auth.route('/logout')
def logout():
    return "test"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")