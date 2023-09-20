import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Replace '/static' with the actual directory you want to serve
        if path.startswith('/tensorboard/65013b711615854054c3bf52'):
            print("YES")
            path = path[len('/tensorboard/65013b711615854054c3bf52'):]
        return http.server.SimpleHTTPRequestHandler.translate_path(self, path)

if __name__ == '__main__':
    PORT = 6006
    Handler = MyHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

