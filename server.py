#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Simple Http Server, to handle html file requests
    Modification: 11/09/2017
    Author: J. Júnior
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

class CodeRequestHandler(BaseHTTPRequestHandler):
    #handle get command
    def do_GET(self):
        #where our file is stored
        root_dir = "src/"
        print(root_dir)
        try:
            if self.path.endswith('.html'):
                fl = open(root_dir + self.path) #open the requested file
                #send the code response
                self.send_response(200)
                #send header
                self.send_header('Content-type', 'text-html')
                self.end_headers()
                #send the requested file to client
                self.wfile.write(fl.read())
                fl.close()
                return

        except IOError:
            self.send_error(404, 'file not found :(')

def run():
        address = '127.0.0.1'
        port = 1025
        print('Hello, iam starting http server...')
        #define the ip and port of server
        server_address = (address, port)
        #Create http server
        httpd = HTTPServer(server_address, CodeRequestHandler)
        print('The server is on! Send me requests.')
        httpd.serve_forever()

if __name__ == '__main__':
    run()
