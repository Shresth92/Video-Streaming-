import socket as sct
import cv2
import pickle as pkl
import struct as srt


socket_name = sct.socket(socket.AF_INET,socket.SOCK_STREAM)
setsockopt(socket_name, SOL_SOCKET, SO_REUSEADDR)

port = 3333
address = ('0000.0000.00.0000',port)

socket_name.bind(address)
socket_name.listen(5)

while True:
        client_socket, addr = socket_name.accept()
  
        if client_socket:
            vid = cv2.VideoCapture(0)
            
            while(vid.isOpened()):
                img,frame = vid.read()
                a = pkl.dumps(frame)
                message = srt.pack("Q",len(a))+a
                socket_name.sendall(message)
                cv2.imshow('TRANSMITTING VIDEO',frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    cv2.release()
