#!/usr/bin/pyton3

import socket

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("Enter the IP you want to connect to: ")
port= int(input("Enter the Port you want to connect to: "))

clientsocket.connect((host,port))

message= clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
