from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest Fitness DevOps Application Running"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/clients")
def clients():
    data = [
        {"name": "Ravi", "program": "Fat Loss"},
        {"name": "Anita", "program": "Muscle Gain"},
        {"name": "John", "program": "Beginner"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)