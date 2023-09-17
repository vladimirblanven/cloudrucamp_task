from http.server import HTTPServer, BaseHTTPRequestHandler
from socket import gethostname
import os, uuid

HOST = "0.0.0.0"
PORT = 8000

class myTestServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        if self.path == '/hostname':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            hostname = os.environ.get('HOSTNAME', str(gethostname()))
            self.wfile.write(bytes(hostname, "utf-8"))
        
        elif self.path == '/author':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            author = os.environ.get('AUTHOR', 'Vladimir')
            self.wfile.write(bytes(author, "utf-8"))
            
        elif self.path == '/id':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            id = os.environ.get('UUID', str(uuid.uuid1()))
            self.wfile.write(bytes(id, "utf-8"))
        
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Wrong /GET !", "utf-8"))

server = HTTPServer((HOST, PORT), myTestServer)
print("Server is running...")

server.serve_forever()

server.serve_close()
print("Server has stopped!")
