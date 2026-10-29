from socket import *
import sys

DEFAULT_IP = "192.168.0.133"
MAX_PORT = 65535

args = sys.argv

#      0         1           2          3 
# server.py server_host server_port filename

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


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

while True:
    print("Ready to serve...")

    (host_addr, port) = server_socket.accept()

    try:
        message = host_addr.recv(1024).decode()
        f = open(file_name)
        output_data = f.read()
        f.close()

        # send HTTP header line
        ok_header = "HTTP/1.1 200 OK\r\n"
        host_addr.send(ok_header.encode())

        # send the file content
        for c in output_data:
            host_addr.send(c.encode())

        host_addr.send("\r\n".encode())

        print(f"link: http://{server_ip}:{server_port}{file_name}")
        host_addr.close()

    except IOError:
        error_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        host_addr.send(error_header.encode())

        host_addr.close()

server_socket.close()
sys.exit()

