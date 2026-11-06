from socket import *
import sys
import time

MAX_PORT = 65535
DEFAULT_CLIENT_NAME = "daniel http client"
args = sys.argv

#      0         1           2          3 
# client.py server_host server_port filename 

if len(args) < 4:
    print(f"Usage: {args[0]} <HOST> <PORT> <FILENAME> [CLIENTNAME]")
    print("<> = required")
    print("[] = optional")

    sys.exit()

server_ip = args[1]
server_port = int(args[2])
file_name = args[3]

if len(args) > 4:
    client_name = args[4]
else:
    client_name = DEFAULT_CLIENT_NAME


if server_port < 0 or server_port > MAX_PORT:
    print(f"Error: Invalid port number {server_port}")
    print(f"Port number must between 0 and {MAX_PORT}")
    sys.exit()


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

query_msg = f"""
GET /{file_name} HTTP/1.1\r
Host: 192.168.0.133:8080\r
User-Agent: {client_name} \r
Accept: text/html\r
Accept-Language: en-US,en;q=0.9\r
Connection: keep-alive\r
\r\n
"""

time.sleep(3)
client_socket.send(query_msg.encode())
print("Sent query:")
print(query_msg)

response_msg = client_socket.recv(1024).decode()
print("Received response: ")
print(response_msg)

client_socket.close()

