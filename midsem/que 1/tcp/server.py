from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print (ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()
     
     abc = connectionSocket.recv(1024).decode()
     capitalizedabc = abc.upper()
     connectionSocket.send(capitalizedabc.encode())
     connectionSocket.close()
