from flask import Flask, jsonify, request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route("/add", methods=["POST"])
def add():
    ans = 0
    try:
        # get the value of the two fields
        num_1 = request.form.get("num1") or "0"
        num_2 = request.form.get("num2") or "0"

        # convert to float (throw error when there is an invalid value)
        num_1 = float(num_1)
        num_2 = float(num_2)
        
        ans = num_1 + num_2
        err = ""
    except ValueError as e:
        err = "Invalid value given. Please only input numbers."
    except Exception as e:
        err = "An error has occurred. Please only input numbers."
    
    response_body = {"answer": ans, "error": err}
    return jsonify({"data": response_body})

@api.route("/subtract", methods=["POST"])
def subtract():
    ans = 0
    try:
        # get the value of the two fields
        num_1 = request.form.get("num1") or "0"
        num_2 = request.form.get("num2") or "0"

        # convert to float (throw error when there is an invalid value)
        num_1 = float(num_1)
        num_2 = float(num_2)

        ans = num_1 - num_2
        err = ""
    except ValueError as e:
        err = "Invalid value given. Please only input numbers."
    except Exception as e:
        err = "An error has occurred. Please only input numbers."
    
    response_body = {"answer": ans, "error": err}
    return jsonify({"data": response_body})
