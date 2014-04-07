import StatusPage
import CGIHTTPServer
import sys
import cgi, cgitb
 
class RequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
  global statusPage
  statusPage = StatusPage.StatusPage()

  def do_GET(s):
    if s.path == '/StatusPage.css':
      s.wfile.write(open("StatusPage.css").read())
    elif s.path == '/StatusPage.js':
      s.wfile.write(open("StatusPage.js").read())
    elif s.path == '/favicon.ico':
      s.wfile.write(open("favicon.ico").read())
    else:
      s.send_response(200)
      s.send_header("Content-type", "text/html")
      s.end_headers()
      s.wfile.write(str(statusPage.content()))

  def do_POST(s):    
    form = cgi.FieldStorage(fp=s.rfile,headers=s.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':s.headers['Content-Type'],})
    statusPage.parse(form)
    s.wfile.write(str(statusPage.content()))

if __name__ == '__main__':
  server_address = ('', 8000)
  httpd = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, RequestHandler)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    sys.exit()
