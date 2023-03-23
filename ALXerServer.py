#!/usr/bin/env python3
# This is the ALXer server.py file
import socket
import sys


def server():
    # Create a TCP/IP socket object
    print('Starting the server')
    print('Create the socket')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local host name
    host = socket.gethostname()
    port = 9999

    # Bind the socket to the port
    print('Bind the socket to the port')
    server_address = (host, port)

    print('Starting up on', server_address)
    serversocket.bind(server_address)

    # Specify the number of connections allowed
    print('Listening for incoming connections')
    serversocket.listen(1)
    # print ( "Listening..." )

    while True:
        # Establish and wait for a connection.
        print('Waiting for a connection')
        clientsocket, address = serversocket.accept()
        # print(" Connected to {}" .format(address))
        try:
            print('Connection from', address)
            print('Welcome to ALXer Server!\r\n')

            # Receive the data in small chunks and retransmit it.
            while True:
                data = clientsocket.recv(1024)
                print('Received: ', data)
                if data:
                    response = 'This is response from ALXer server'
                    print('Sending data back to the client :', response)
                    clientsocket.sendall(response.encode())
                else:
                    print('No data from', address)
                    break

                # clientsocket.send(msg.encode('ascii'))
        finally:
            # Clean up the connection.
            clientsocket.close()


if __name__ == '__main__':
    server()
