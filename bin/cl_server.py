#! /usr/bin/env python

import SocketServer

class ClTcpHandler(SocketServer.BaseRequestHandler):
    """
    This is a TCP Request Handler that listens specifically for
    HTTP requests. In these request is a special header called
    "link-tracker".  This essentially tells us which link we have
    just clicked, so we can record it to a file or database
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        for line in self.data.split('\n'):
            # We are looking for our "link-tracker" header
            if 'link-tracker' in line:
                print line

if __name__=='__main__':
    HOST, PORT = 'localhost', 8111
    server = SocketServer.TCPServer((HOST, PORT), ClTcpHandler)
    server.serve_forever()