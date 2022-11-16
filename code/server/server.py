import socket
import os 

s = socket.socket()

host = '' # empty string means server can listen to requests coming from other computers on network 
port = 12345 # reserve a port on our computer.  
s.bind((host, port)) # bind to the port

s.listen(5) # accepts up to 5 connections
print("Socket is listening....")

c, addr = s.accept() # Establish connection with client 
print(addr, "has connected to the server")

file = open('transferfile.txt', 'rb') # open transferfile.txt for reading in binary mode
file_data = file.read(1024) # returns specified number of bytes from the file
c.send(file_data) # send file data to connected socket
file.close()
print("Data has been transmitted successfully")

os.remove('transferfile.txt') # delete file since we've alread transferred data




 

    
