import os 

my_server = Server.Server('', 12345)
my_server.start()

if os.path.isfile('transferfile.txt'):
    my_server.sendFile('transferfile.txt')
else: 
    my_server.receiveFile()
