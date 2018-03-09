import os
import SimpleHTTPServer
import SocketServer

WEB_PORT = os.getenv('WEB_PORT', 8080)
WEB_PATH = os.path.join(os.getcwd(), 'static')


def run_web():
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", WEB_PORT), Handler)

    print "Serving at port {} in path {}".format(WEB_PORT, WEB_PATH)
    os.chdir(WEB_PATH)
    httpd.serve_forever()


def main():
    run_web()


if __name__ == '__main__':
    main()
