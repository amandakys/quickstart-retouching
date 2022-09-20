from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8888

class Handler(SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.wasm'] = 'application/wasm'

httpd = HTTPServer(("", PORT), Handler)
print("Server started http://%s:%s" % ("", PORT))


# httpd = SocketServer.TCPServer(("", PORT), Handler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("Server stopped")