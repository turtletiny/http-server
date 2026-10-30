from socket import *
import sys

MAX_PORT = 65535
args = sys.argv

#      0         1           2          3 
# client.py server_host server_port filename

if len(args) < 4:
    print(f"Usage: {args[0]} [HOST] [PORT] [FILENAME]")
    sys.exit()

server_ip = args[1]
server_port = int(args[2])
file_name = args[3]

if server_port < 0 or server_port > MAX_PORT:
    print(f"Error: Invalid port number {server_port}")
    print(f"Port number must between 0 and {MAX_PORT}")
    sys.exit()


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

query_msg = f"""
    GET /{file_name} HTTP/1.1\r\n
    Host: 192.168.0.133:6969\r\n
    User-Agent: Kitty \r\n
    Accept: text/html\r\n
    Accept-Language: en-US,en;q=0.9\r\n
    Connection: keep-alive\r\n
    \r\n
    """

client_socket.send(query_msg.encode())

response_msg = client_socket.recv(1024).decode()
print(response_msg)

print(client_socket.recv(1024).decode())

client_socket.close()

