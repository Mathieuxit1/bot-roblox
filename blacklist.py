def handler(request):
    if request.method == "POST":
        data = request.json()
        pseudo = data.get("pseudo")

        if pseudo:
            return {
                "statusCode": 200,
                "body": {"status": "ok", "pseudo": pseudo}
            }

    return {
        "statusCode": 400,
        "body": {"status": "error"}
    }