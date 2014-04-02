import StatusPage
import CGIHTTPServer
import sys
import cgi

class MyRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
  global statusPage
  statusPage = StatusPage.StatusPage()

  def do_GET(s):
    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write(str(statusPage.content()))

#  def do_POST(s):    
#    """Respond to a POST request."""
#    form = cgi.FieldStorage(fp=s.rfile,headers=s.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':s.headers['Content-Type'],})
#    s.wfile.write("<html><head><title>Title goes here.</title></head>")
#    s.wfile.write("<body><p>This is a test.</p>")
#    s.wfile.write("<p>You accessed path: %s</p>" % s.path)
#    s.wfile.write("<p>Also, super_important_list is:</p>")
#    s.wfile.write(str(super_important_list))
#    s.wfile.write("<p>Furthermore, you POSTed the following info: ")
#    for item in form.keys():
#      s.wfile.write("<p>Item: " + item)
#    s.wfile.write("<p>Value: " + form[item].value)
#    s.wfile.write("</body></html>")

if __name__ == '__main__':
  server_address = ('', 8000)
  httpd = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    sys.exit()
