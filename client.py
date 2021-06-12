import socket as sct 
import cv2 
import pickle as pkl
import struct s srt

client_socket = sct.socket(socket.AF_INET,socket.SOCK_STREAM) 
setsockopt(client_socket, SOL_SOCKET, SO_REUSEADDR) 

host_ip = '000.000.00.000' 
port = 3333

client_socket.connect( (host_ip, port) )

data = b""
payload_size = srt.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = srt.unpack("Q",packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pkl.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_socket.close()
