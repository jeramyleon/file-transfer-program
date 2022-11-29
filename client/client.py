import os 
from client_class import Client 

client = Client('127.0.0.1', 12345)
client.connect()

if os.path.isfile('transferfile.txt'):
    client.sendFile('transferfile.txt')
else: 
    client.receiveFile()
    
