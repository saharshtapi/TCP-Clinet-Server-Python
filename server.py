#!/usr/bin/python2

#Simple tcp server.
import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = socket.gethostbyname() //to get automatically
host= '192.168.1.68'
port = 4444

serversocket.bind((host,port))

serversocket.listen(3)

while True:
	clientsocket, address=serversocket.accept()

	print("Receive connectioin from %s " % str(address))

	message= 'Thnk you for connection to the server' + "\r\n"
	clientsocket.send(message)

	clientsocket.close() 