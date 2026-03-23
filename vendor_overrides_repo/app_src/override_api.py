#!/usr/bin/env python3
from flask import Flask, request, jsonify
import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OVERRIDE_FILE = os.path.join(BASE_DIR, "local_overrides.json")

app = Flask(__name__)

def load():
    if not os.path.exists(OVERRIDE_FILE):
        return {}
    with open(OVERRIDE_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(OVERRIDE_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.get("/overrides")
def get_overrides():
    return jsonify(load())

@app.post("/overrides")
def update_override():
    data = load()
    prefix = request.json.get("prefix", "").lower()
    vendor = request.json.get("vendor", "")
    if prefix and vendor:
        data[prefix] = vendor
        save(data)
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
