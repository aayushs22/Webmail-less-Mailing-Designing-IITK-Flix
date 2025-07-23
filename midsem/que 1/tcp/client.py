from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
abc = input('please enter lowercase ')
clientSocket.send(abc.encode())
newabc = clientSocket.recv(1024)
print ('the message from server', newabc.decode())
clientSocket.close()
