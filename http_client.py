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
