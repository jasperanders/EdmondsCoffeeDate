from flask import Flask, request
import json
import requests


app = Flask(__name__)


@app.route(f"/", methods=["POST"])
def fwd_to_lambda():
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
    forward = {"body": json.dumps(req)}

    resp = requests.post(
        "http://localhost:9000/2015-03-31/functions/function/invocations", json=forward
    ).json()
    return resp

