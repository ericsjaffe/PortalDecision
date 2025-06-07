from flask import Flask, jsonify, render_template
from scraper import get_transfer_updates

app = Flask(__name__)

@app.route("/")
def index():
    updates = get_transfer_updates()
    return render_template("index.html", updates=updates)

@app.route("/api/updates")
def api_updates():
    return jsonify(get_transfer_updates())

if __name__ == "__main__":
    app.run(debug=True)
