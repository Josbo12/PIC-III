import socket
import sys
import psutil
import unittest
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

# Listen for incoming connections
sock.listen(1)

while True:
# Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    #accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().

    try:
        print >>sys.stderr, 'connection from', client_address

        data = connection.recv(1024)

        if data == "CPU":

            message = '"CPU:' + str(psutil.cpu_percent()) + "%" +'"'
            print >>sys.stderr, message
            print >>sys.stderr, 'sending data back to the client'




        elif data == "MEM":
            message = '"MEM:' + str(psutil.virtual_memory().percent) + "%" +'"'
            print >>sys.stderr, message
            print >>sys.stderr, 'sending data back to the client'



        else:
            message = 'ERR unknown command'
            print >>sys.stderr, 'ERROR "%s"'
            print >>sys.stderr, 'sending data back to the client'

        connection.sendall(message)

    finally:
        # Clean up the connection
        connection.close()
