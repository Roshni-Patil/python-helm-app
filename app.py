from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps World 🚀"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "hostname": socket.gethostname(),
        "time": str(datetime.datetime.now())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)