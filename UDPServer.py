from socket import *
import time

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('192.168.0.133', server_port))
print("UDP Serve is ready and listening")

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper().encode()
    print(f"got the msg at : {modified_message}")

    server_socket.sendto(modified_message, client_address)
