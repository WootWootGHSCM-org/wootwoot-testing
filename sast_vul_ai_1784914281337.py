from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the sample app"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(data)


if __name__ == "__main__":
    # FIXED: bind only to localhost. For external access, run behind a
    # production WSGI server (e.g. Gunicorn/uWSGI) fronted by a reverse
    # proxy, instead of exposing the Flask dev server directly.
    app.run(debug=False, host="127.0.0.1")
