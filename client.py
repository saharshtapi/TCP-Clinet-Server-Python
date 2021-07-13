#!/usr/bin/pyton2

import socket

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.1.68'
port= 4444

clientsocket.connect((host,port))

message= clientsocket.recv(1024)

clientsocket.close()

print(message)