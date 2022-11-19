import socket
import os 

"""
s = socket.socket()

host = '' # empty string means server can listen to requests coming from other computers on network 
port = 12345 # reserve a port on our computer.  
s.bind((host, port)) # bind to the port

s.listen(5) # accepts up to 5 connections
print("Socket is listening....")

c, addr = s.accept() # Establish connection with client 
print(addr, "has connected to the server")

if os.path.isfile('transferfile.txt'): # if transferfile.txt exists in directory

    file = open('transferfile.txt', 'rb') # open transferfile.txt for reading in binary mode
    file_data = file.read(1024) # returns specified number of bytes from the file
    c.send(file_data) # send file data to connected socket
    file.close()
    print("Data has been transmitted successfully")

    os.remove('transferfile.txt') # delete file since we've already transferred data
else:

    filename = input(str("Please enter a filename for the incoming file: "))
    file = open(filename, 'wb') # open new file for writing in binary mode 
    file_data = c.recv(1024)    # receive file data  
    file.write(file_data)       # write file data to file 
    file.close() 
    print("File has been received successfully")
"""

class Server:
    def __init__(self, host, port):
        """Initialize server."""

        self.s = socket.socket()
        self.host = host 
        self.port = port 
        self.s.bind((self.host, self.port))

    def start(self):
        """Listen for connections and establish connections."""
        
        self.s.listen(5) # Accepts 5 connections.
        print("Server is listening...")

        c, addr = self.s.accept() # Establish connection with client.
        print(addr, "has connected to the server.")

        return True 
    
    def sendFile(self):
        pass 

    def receiveFile(self):
        pass 

server = Server('', 12345)
server.start()
