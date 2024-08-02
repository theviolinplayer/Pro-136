from flask import Flask, render_template, jsonify, request
from data import data
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"success"
    }), 200

@app.route("/planet")
def planet():
    planet_name = request.args.get("name")
    for item in data:
        if item["name"] == planet_name:
            return jsonify({
            "data":item,
            "message":"success"
            }), 200

app.run(debug=True)