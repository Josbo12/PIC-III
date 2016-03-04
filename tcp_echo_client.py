import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = sys.argv[1]
MEMCPU = sys.argv[2]

# Connect the socket to the port where the server is listening

if MEMCPU == "CPU":
    message = "CPU"
elif MEMCPU == "MEM":
    message = "MEM"
else:
    message = "ERROR"


server_address = (ip, 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.

try:

    sock.sendall(message)
    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
