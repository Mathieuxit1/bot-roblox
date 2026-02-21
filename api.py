from flask import Flask, jsonify, request

app = Flask(__name__)

messages = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data["message"])
    return {"status": "ok"}

@app.route("/get", methods=["GET"])
def get():

    if messages:
        return {"message": messages.pop(0)}

    return {"message": None}

app.run(host="0.0.0.0", port=10000)