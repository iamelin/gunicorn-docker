def app(environ, start_response):
    data = b"Hello, World!\n"

    start_response("200 OK", [
        ("Context-Type", "text/plain"),
        ("Context-Length", str(len(data)))
    ])
    return iter([data])
