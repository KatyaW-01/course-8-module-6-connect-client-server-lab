# Flask + JavaScript Event Tracker

This lightweight web app connects a front end built with HTML and JavaScript to a back end powered by Flask. It allows users to view a list of events and add new ones through a simple interface.

## Lab Objectives

- Set up a Flask server that handles both `GET` and `POST` requests.
- Use the JavaScript `fetch()` API to send and receive JSON data.
- Return consistent JSON responses from Flask routes.
- Dynamically render and update content on the front end based on back-end data.

## How It Works

### Back End (`server.py`)

- Built using **Flask**.
- Handles routes:
  - `GET /events` – returns the current list of events.
  - `POST /events` – adds a new event with a unique `id` and `title`.
- Adds CORS headers to allow communication with the front end.
- Returns all data in JSON format.

### Front End (`script.js`)

- On page load, fetches the list of events and renders them to the DOM.
- Listens for form submissions to add new events.
- Sends `POST` requests with JSON to the server and dynamically updates the event list.

## Files

- `server.py`: Flask app that serves and manages event data.
- `data.py`: Contains a list of initial events
- `script.js`: JavaScript logic for fetching and submitting events.
- `index.html`: HTML structure with a form and a list to display events.

## File Structure
```
.
├── client/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── server.py
|__ data.py
|
├── tests/
│   └── test_app.py
├── Pipfile
├── Pipfile.lock
├── README.md
```
## Prerequisites
* Python 3.x installed on your system
* Flask
  ```bash
  pip install flask
  ```
  

## Running the App

1. **Start the Flask server**  
   In your terminal, run:
   ```bash
   python server.py
   ```
   The server will be available at http://127.0.0.1:5000
2. Open `index.html` in your browser
3. Add and View Events
