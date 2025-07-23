import cv2
import numpy as np
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
cap= cv2.VideoCapture(0)
connectionSocket, addr = serverSocket.accept()
while True:
     ret,frame=cap.read()
     connectionSocket.send(frame.encode())
     if cv2.waitKey(1) & 0xFF==ord('q'):
        break
connectionSocket.close()
cap.release()  

cv2.destroyAllWindows() 
 