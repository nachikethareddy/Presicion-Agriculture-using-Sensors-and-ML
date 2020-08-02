from http.server import HTTPServer, BaseHTTPRequestHandler
 
class web_server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
    def do_GET(self):
        self.do_HEAD()
        file=open("roverstatus.txt","r")
        a=int(file.read())
        file.close()
        print(a)
        a=a+1
        file=open("roverstatus.txt","w+")
        file.write(str(a))
        file.close()
        if self.path == '/':
                file=open("path.txt","r")
                q=file.read()
                file.close()
                if(q!=""):
                    q=[str(x) for x in q.split(" ")]
                    r=q.pop()
                    q=" ".join(str(x) for x in q)
                    file=open("path.txt","w+")
                    file.write(q)
                    file.close()                    
                else:
                    r='0'
                self.wfile.write(r.encode('utf-8'))

httpd = HTTPServer(('192.168.43.133',80), web_server)
httpd.serve_forever()
