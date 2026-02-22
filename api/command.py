import json

data_memory = {}

def handler(request):

    if request.method == "POST":
        body = request.json()
        command = body.get("command")
        player = body.get("player")

        data_memory["command"] = command
        data_memory["player"] = player

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "saved"})
        }

    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(data_memory)
        }