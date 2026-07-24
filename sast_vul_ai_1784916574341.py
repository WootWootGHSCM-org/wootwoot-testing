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
    # VULNERABLE: binding to 0.0.0.0 with debug=True exposes the dev server
    # to the entire network and enables the Werkzeug debugger.
    # semgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(debug=True, host="0.0.0.0")
