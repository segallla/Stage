import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from bess.pipeline import analyze_address


HTML_FORM = """<!DOCTYPE html>
<html>
<head>
    <title>BESS Analysis</title>
</head>
<body>
    <h1>BESS Address Analysis</h1>
    <form action="/analyze" method="get">
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" size="50" />
        <input type="submit" value="Analyze" />
    </form>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_FORM.encode("utf-8"))
            return
        if parsed.path == "/analyze":
            params = parse_qs(parsed.query)
            address = params.get("address", [""])[0]
            if not address:
                self.send_response(400)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Missing address parameter")
                return
            try:
                result = analyze_address(address)
                result_json = json.dumps(result, indent=2)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(result_json.encode("utf-8"))
            except ValueError as exc:
                self.send_response(400)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(str(exc).encode("utf-8"))
            return
        self.send_response(404)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=Handler, host="0.0.0.0", port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on http://{host}:{port} ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
