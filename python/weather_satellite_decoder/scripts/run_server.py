import http.server
import socketserver

def run_server():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server running at port", PORT)
        httpd.serve_forever()

run_server()
