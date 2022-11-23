import socket 
import os 

class Client: 
    def __init__(self, host, port):
        """Initialize client object and define which host and port we want to connect to."""

        self.s = socket.socket()
        self.host = host 
        self.port = port

    def connect(self):
        """Connect to specified host and port."""

        self.s.connect((self.host, self.port))
        print("connected")

        return True   

    def sendFile(self, filename):
        """Send file over network."""

        file = open(filename, 'rb') # open file for reading in binary mode
        file_data = file.read(1024) # returns specified number of bytes from file
        self.s.send(file_data) # send file data to connected socket
        file.close() 

        os.remove(filename) # delete file since we've already transferred
        print("File sent successfully.") 
        return True
    
    def receiveFile(self):
        """Receive file over network."""

        filename = input(str("Please enter a filename for the incoming file: "))
        file = open(filename, 'wb') # open new file for writing in binary mode 
        file_data = self.s.recv(1024)    # receive file data from server 
        file.write(file_data)       # write file data to file 
        file.close() 

        print("File received successfully.")
        return True

 
client = Client('127.0.0.1', 12345)
client.connect()

if os.path.isfile('transferfile.txt'):
    client.sendFile('transferfile.txt')
else: 
    client.receiveFile()
    
