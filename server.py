#!/usr/bin/python3

#Simple tcp server.
import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = socket.gethostbyname() //to get automatically
host= input("Enter the IP you want to listen on: ")
port = int(input("Enter the Port you want to listen on:"))

serversocket.bind((host,port))

serversocket.listen(3)

while True:
	try:
		clientsocket, address=serversocket.accept()

		print("Receive connectioin from " ,str(address))

		message= 'Thnk you for connection to the server' + "\r\n"
		clientsocket.send(message.encode('ascii'))

		clientsocket.close() 
	except:
		exit()
