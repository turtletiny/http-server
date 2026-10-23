from socket import *

server_name = '192.168.0.133'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM) #AF_INET = IPv4, SOCK_DGRAM = UDP socket
message = input("enter a sentence")
client_socket.sendto(message.encode(), (server_name, server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()
