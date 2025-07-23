
import cv2
import numpy as np
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
    meta = clientSocket.recv(1024)
    cv2.imshow('original',meta.decode())
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
clientSocket.close()
cap.release()  
#out.release()  
cv2.destroyAllWindows() 