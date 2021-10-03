from flask import Flask, request
from app.coffedatematching import compute_coffee_dates

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Find coffee matching under /match'


@app.route('/matching', methods=['POST'])
def matching():
    requ = request.json

    matches = compute_coffee_dates(requ["people"], 2)

    print(matches)
    return {'matches': matches}
