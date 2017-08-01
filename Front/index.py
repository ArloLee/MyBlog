#!/usr/bin/python

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import socket
import fcntl
import struct
import pickle
from datetime import datetime
from collections import OrderedDict

class HandlerClass(SimpleHTTPRequestHandler):
    def get_ip_address(self,ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
        )[20:24])
    def log_message(self,format, *args):
        if len(args) < 3 or "200" not in args[1]:
            return
        try:
            request = pickle.load(open("pickle_data.txt","r"))
        except:
            request=OrderedDict()
        time_now = datetime.now()
        ts = time_now.strftime('%Y-%m-%d %H:%M:%S')
        server = self.get_ip_address('eno16777736')
        host = self.address_string()
        addr_pair = (host,server)
        if addr_pair not in request:
            request[addr_pair]=[1,ts]
        else:
            num = request[addr_pair][0]+1
            del request[addr_pair]
            request[addr_pair]=[num,ts]
        file = open("index.html","w")
        file.write("<html><body><center><h1>webpage visite results</center></body></html>")
        for pair in request:
            if pair[0] == host:
                guest = "Local:" + pair[0]
            else:
                guest = pair[0]
            if (time_now-datetime.strptime(request[pair][1],'%Y-%m-%d %H:%M:%S')).second <3:
                file.write("<p>#"+ str(request[pair][1]) + ":" + str(request[pair][0]))
            else:
                file.write("from werwerwerawer else")
        file.close()
        pickle.dump(request,open("pickle_data.txt","w"))

if __name__ == "__main__":
    try:
        ServerClass = BaseHTTPServer.HTTPServer
        Protocol = "HTTP/1.0"
        addr = len(sys.argv) <2 and "0.0.0.0" or sys.argv[1]
        port = len(sys.argv) <3 and 90 or int(sys.argv[2])
        HandlerClass.protocol_version = Protocol
        httpd = ServerClass((addr,port),HandlerClass)
        sa = httpd.socket.getsockname()
        print "serving http on ", sa[0],"port",sa[1],"..."
        httpd.serve_forever()
    except:
        exit()