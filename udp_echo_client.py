#The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.

import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = sys.argv[1]
MEMCPU = sys.argv[2]


server_address = (ip, 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address

if MEMCPU == "CPU":
    message = "CPU"
elif MEMCPU == "MEM":
    message = "MEM"
else:
    message = "ERROR"


try :
        #Set the whole string
        sock.sendto(message, server_address)

        # receive data from client (data, addr)
        d = sock.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print 'Server reply : ' + reply

finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
