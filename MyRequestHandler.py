import StatusPage
import CGIHTTPServer
import sys
import cgi, cgitb

 
class MyRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
  global statusPage
  statusPage = StatusPage.StatusPage()

  def do_GET(s):
    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write(str(statusPage.content()))

  def do_POST(s):    
    """Respond to a POST request."""
    form = cgi.FieldStorage(fp=s.rfile,headers=s.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':s.headers['Content-Type'],})
    statusPage.parse(form)
    s.wfile.write(str(statusPage.content()))

if __name__ == '__main__':
  server_address = ('0.0.0.0', 8000)
  httpd = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    sys.exit()
