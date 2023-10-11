import http.server
import socketserver
import json

# Define the handler for our HTTP server
class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Check if the path is /hello
        if self.path == '/':
            # Prepare the response as JSON
            response = json.dumps({
                'message': 'Hello, World!'
            }).encode('utf-8')
            
            # Send the headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(response))
            self.end_headers()
            
            # Send the response body
            self.wfile.write(response)
        else:
            # For other paths, send a 404 response
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# Run the server
PORT = 80
with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
