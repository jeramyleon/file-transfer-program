import socket
import os

class Server:
    def __init__(self, host, port):
        """Initialize server."""

        self.s = socket.socket()
        self.host = host 
        self.port = port 
        self.s.bind((self.host, self.port))

    def start(self):
        """Listen for connections and establish connections."""
        
        self.s.listen(5)               # Accepts 5 connections.
        print("Server is listening...")

        self.c, addr = self.s.accept() # Establish connection with client.
        print(addr, "has connected to the server.")

        return True 
    
    def sendFile(self, filename):
        """Send file through network."""

        file = open(filename, 'rb') # open transferfile.txt for reading in binary mode
        file_data = file.read(1024)           # returns specified number of bytes from the file
        self.c.send(file_data)                # send file data to connected socket
        file.close()
        print("Data has been transmitted successfully")

        os.remove(filename)         # delete file since we've already transferred data
        return True 

    def receiveFile(self):
        """Receive file through network."""

        filename = input(str("Please enter a filename for the incoming file: "))
        file = open(filename, 'wb')      # open new file for writing in binary mode 
        file_data = self.c.recv(1024)    # receive file data  
        file.write(file_data)            # write file data to file 
        file.close() 
        print("File has been received successfully")

        return True 