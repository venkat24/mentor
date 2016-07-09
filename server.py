import SimpleHTTPServer
import SocketServer
PORT = 7200
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Listening on port", PORT
httpd.serve_forever()