import flask
import requests
import json
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getmethod/<jsdata>")
def getJSData():
    headers = {"Authorization": "Bearer 4e1b9114e2a8f946fe095f961b3a3d88"}
    r = requests.get(
        "https://api.pledge.to/v1/organizations",
        headers=headers
    ).json()
    return r
