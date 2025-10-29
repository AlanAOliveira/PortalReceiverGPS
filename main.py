from http.server import HTTPServer as BaseHTTPServer, SimpleHTTPRequestHandler
import simplejson
import os
import data as dados
import htmlfunctions
import DB
import socket

#python -m eel main.py web --onefile
class HTTPHandler(SimpleHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def translate_path(self, path):
        path = SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        #self.send_response(200)
        self.end_headers()
        data = simplejson.loads(self.data_string)
        print(data["function"])

        if data["function"] == "enviarListaYG":
            self.wfile.write(
                bytes(htmlfunctions.enviarListaYG(data["dados"]), "utf-8"))
            return
        
        if data["function"] == "getYGBarcode":
            self.wfile.write(
                bytes(htmlfunctions.getYGBarcode(data["dados"]), "utf-8"))
            return
         
class HTTPServer(BaseHTTPServer):

    def __init__(self,
                 base_path,
                 server_address,
                 RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        BaseHTTPServer.__init__(self, server_address, RequestHandlerClass)


web_dir = os.path.join(os.path.dirname(__file__), 'web')
httpd = HTTPServer(web_dir, (socket.gethostname(), 80))
#httpd = HTTPServer(web_dir, ("10.253.145.53", 80))

print(socket.gethostname())
httpd.serve_forever()
