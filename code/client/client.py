import socket 

s = socket.socket()
port = 12345                   # define port we want to connect to
s.connect(('127.0.0.1', port)) # connect to server on local computer 
print("connected")

filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename, 'wb') # open new file for writing in binary mode 
file_data = s.recv(1024) # receive file data from server 
file.write(file_data) # write file data to file 
file.close() 
print("File has been received successfully")





