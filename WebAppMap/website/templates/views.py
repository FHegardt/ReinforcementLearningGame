from flask import Blueprint
from ....Snakemap import Agent
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return agent.Agent
