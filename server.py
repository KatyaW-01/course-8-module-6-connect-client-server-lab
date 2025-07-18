from flask import Flask, jsonify, request
from data import events

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message='Welcome')

@app.route("/events", methods = ["GET"])
def get_events():
    return jsonify(events)

@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    new_id = max((event["id"] for event in events), default=0) + 1
    if data and "title" in data:
        new_event = {"id": new_id, "title": data["title"]}
        events.append(new_event)
        return jsonify(new_event), 201
    return "", 400

if __name__ == "__main__":
    app.run(debug=True)
