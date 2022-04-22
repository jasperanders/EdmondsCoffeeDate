from flask import Flask, request
from logic.coffedatematching import compute_coffee_dates

app = Flask(__name__)
version = "v1"


@app.route("/")
def hello():
    return "Find coffee matching under /v1/matching"


@app.route(f"/{version}/matching", methods=["POST"])
def matching():
    """
    this route accepts an JSON array of groups. Each group is an array of individuals. Also an amount, that results in 
    the number matchings.
    E.g.:
    ```
    {   
        "amount": 2,
        "groups": [
            [
                "Jasper Anders",
                "Hannes von Boetticher"
            ],  
            [
                "Pert Gubbi",
                "Bob Senrie"
            ]
        ]
    }
    ```
    """

    req = request.json

    matches = compute_coffee_dates(req["groups"], req["amount"])

    print(matches)
    return {"matches": matches}


@app.route(f"/{version}/slack", methods=["POST"])
def slack_hello():
    requ = request.json

    return {"challenge": requ["challenge"]}
