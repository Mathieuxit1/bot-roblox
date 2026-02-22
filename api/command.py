import json

memory = {}

def handler(request):

    if request.method == "POST":
        data = request.json()

        memory["command"] = data.get("command")
        memory["player"] = data.get("player")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "saved"})
        }

    if request.method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(memory)
        }