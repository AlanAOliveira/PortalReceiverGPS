# python -m http.server 8000 --directory ./web

from http.server import HTTPServer as BaseHTTPServer, SimpleHTTPRequestHandler
import simplejson
import os
import data as dados
import htmlfunctions
import ssl
import socket

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

        if data["function"] == "getLista":
            self.wfile.write(
                bytes(htmlfunctions.geralistapecas(), "utf-8"))
            return
        
        if data["function"] == "getListaSingle":
            self.wfile.write(
                bytes(htmlfunctions.geralistasingle(), "utf-8"))
            return
        
        if data["function"] == "salvaLista":
            self.wfile.write(
                bytes(htmlfunctions.salvaLista(data["dados"]), "utf-8"))
            return
        
        if data["function"] == "salvaListaSingle":
            self.wfile.write(
                bytes(htmlfunctions.salvaListaSingle(data["dados"]), "utf-8"))
            return
        
        if data["function"] == "relatorioFinal":
            self.wfile.write(
                bytes(htmlfunctions.relatorioFinal(), "utf-8"))
            return

        else:
            with open("for_presen.py", 'rb') as f:
                self.wfile.write(f.read())
            return
         
class HTTPServer(BaseHTTPServer):

    def __init__(self,
                 base_path,
                 server_address,
                 RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        BaseHTTPServer.__init__(self, server_address, RequestHandlerClass)


web_dir = os.path.join(os.path.dirname(__file__), 'web')
httpd = HTTPServer(web_dir, (socket.gethostname(), 8444))
print(socket.gethostname())
httpd.serve_forever()
