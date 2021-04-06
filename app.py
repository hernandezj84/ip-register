import json
from flask import Flask, jsonify, request, make_response, request
from flask_cors import CORS
import json
from database import Database


app = Flask(__name__)
app.config["JSON_SOR_KEYS"] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
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
    dict_headers = {r[0]: r[1]for r in list(request.headers)}
    return make_response(jsonify(database.insert_ip(ip_address, json.dumps(dict_headers))))
