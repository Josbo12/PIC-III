import socket
import sys
import psutil
import unittest
import re



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, 'waiting for a connection'
    d = sock.recvfrom(1024)
    data = d[0]
    addr = d[1]





    if data == "MEM":
        message = '"MEM:' + str(psutil.virtual_memory().percent) + "%" +'"'
        print >>sys.stderr, message
        print >>sys.stderr, 'sending data back to the client'

    elif data == "CPU":
        #CPU = psutil.cpu_percent()
        message = '"CPU:' + str(psutil.cpu_percent()) + "%" +'"'
        print >>sys.stderr, message
        print >>sys.stderr, 'sending data back to the client'


    else:
        message = 'ERR unknown command'
        print >>sys.stderr, 'ERROR'
        print >>sys.stderr, 'sending data back to the client'

    if data:
        sock.sendto(message, addr)


sock.close()
