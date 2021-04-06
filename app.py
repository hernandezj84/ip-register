import json
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from database import Database

app = Flask(__name__)
app.config["JSON_SOR_KEYS"] = False
app.config["CORS_HEADERS"] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/test/")
def test():
    return make_response(jsonify({"message": 'OK'}))

@app.route("/list-ip/")
def ip_list():
    """Returns ip list from database
    """
    database = Database()
    data = database.get_list_ip()
    return make_response(jsonify(data))

@app.route("/register-ip/<ip_address>/", methods=(['GET', ]))
def register_ip(ip_address):
    """Register an ip address

    Args:
        ip_address (str): ip address from user
    """
    database = Database()
    return make_response(jsonify(database.insert_ip(ip_address)))
