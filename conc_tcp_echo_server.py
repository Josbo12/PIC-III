import socket
import sys
import psutil
import unittest
import re
import Cliente


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


    #accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().



# bucle para atender clientes
    while 1:
      # Se espera a un cliente
      connection, client_address = sock.accept()
      # Se escribe su informacion
      print "conectado "+str(client_address)
      # Se crea la clase con el hilo
      hilo = Cliente(connection, server_address)
      # y se arranca el hilo
      hilo.start()
