#!/usr/bin/python
import StatusPage
import CGIHTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import sys
import cgi, cgitb

class RequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
  global statusPage
  statusPage = StatusPage.StatusPage()

  def __init__(self, request, client_address, server):
    CGIHTTPServer.CGIHTTPRequestHandler.__init__(self, request, client_address, server)

  def do_GET(s):
    if s.path == '/':
      s.send_response(200)
      s.send_header("Content-type", "text/html")
      s.end_headers()
      s.wfile.write(str(statusPage.content()))
    elif s.path == '/update':
      s.send_response(200)
      s.send_header("Content-type", "text/html")
      s.end_headers()
      s.wfile.write(str(statusPage.update()))
    else:
      CGIHTTPServer.CGIHTTPRequestHandler.do_GET(s)

  def do_POST(s):    
    form = cgi.FieldStorage(fp=s.rfile,headers=s.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':s.headers['Content-Type'],})
    statusPage.parse(form)
    s.wfile.write(str(statusPage.content()))

if __name__ == '__main__':
  server_address = ('0.0.0.0', 3674)
  httpd = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, RequestHandler)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    statusPage.exit()
    sys.exit()

