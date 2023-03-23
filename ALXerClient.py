#!/usr/bin/env python3
# This is ALXer web server client.py file
import socket
import sys


def client():
    # Create a TCP/IP socket object
    print('Starting Client')
    print('Create a TCP/IP socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 9999
    server_address = (host, port)
    # Connect the socket to the port where the server is listening.
    print('Connecting the socket to the server port')
    print('Connecting to: ', server_address)
    sock.connect(server_address)
    print('Connected to server')

    try:
        # Send data.
        print('Send data')
        message = 'This is the message. It will be repeated.'
        print('Sending :', message)
        sock.sendall(message.encode())

        # Look for the response.
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024).decode()
            amount_received += len(data)
            print('Received from server :', data)
    finally:
        print('Closing socket')
        sock.close()


if __name__ == '__main__':
    client()
