from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Item added to cart" },
    {"id": 2, "title": "Order placed"}
]

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route("/")
def home():
    return jsonify(message='Welcome')

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route("/events", methods = ["GET"])
def get_events():
    return jsonify(events)

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201

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
