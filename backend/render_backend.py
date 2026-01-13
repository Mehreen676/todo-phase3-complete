# SIMPLE BACKEND - No dependencies
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = {"status": "running", "service": "Todo Backend"}
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = {"response": "Task added", "tools": ["add_task"]}
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), TodoHandler)
    server.serve_forever()