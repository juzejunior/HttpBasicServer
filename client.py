#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Simple Http Client, to request html files
    Modification: 11/09/2017
    Author: J. Júnior
'''
import httplib
import sys

#get http server ip - pass in the command line
http_server = sys.argv[1]
#create a connection with the server
conn = httplib.HTTPConnection(http_server)

while 1:
   cmd = raw_input('input command (ex. GET index.html): ')
   cmd = cmd.split()

   if cmd[0] == 'exit': #type exit to end it
    break
   #request command to server
   conn.request(cmd[0], cmd[1])
   #get response from server
   rsp = conn.getresponse()
   #print server response and data
   print(rsp.status, rsp.reason)
   print(rsp.getheaders())
   data_received = rsp.read()
   print(data_received)

#close connection
conn.close()
