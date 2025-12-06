payloads = []

def handler(request):
    method, path = request.split(" ", 1)

    if method == "GET" and path.startswith("/items-status="):
        status = path.split("=", 1)[1]
        return [b for b in payloads if b["status"] == status]


    if method == "GET" and path == "/items":
        return payloads

    if method == "GET" and path == "/items/count":
        return len(payloads)

    if method == "POST" and path == "/items":
        payloads_id = len(payloads) + 1
        payloads.append({"id": payloads_id, "name": f"payload {payloads_id}", "status": "available","Name": "James"})
        return "Payload added successfully"

    return "Unknown request"

print(handler("POST /items"))
print(handler("GET /items"))
print(handler("GET /items/count"))
print(handler("GET /items-status=checked_out"))



