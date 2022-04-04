from flask import Blueprint, render_template
import sys
sys.path.append('./SnakeMap')
import agent

def StartSnake():
    return agent.train()


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "test"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/snake')
def snake():
    return render_template("reinforcement_snake.html", StartSnake = StartSnake)