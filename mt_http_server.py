from socket import *
import sys

DEFAULT_IP = "192.168.0.133"

args = sys.argv

#      0         1           2          3 
# server.py server_host server_port filename

if len(args) < 4:
    print(f"Usage: {args[0]} [HOST] [PORT] [FILENAME]")
    sys.exit()

server_ip = args[1]
server_port = int(args[2])
file_name = args[3]

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

while True:
    print("Ready to serve...")

    connection_socket = server_socket.accept()[0]

    try:
        message = connection_socket.recv(1024).decode()
        f = open(file_name)
        output_data = f.read()
        f.close()

        # send HTTP header line
        ok_header = "HTTP/1.1 200 OK\r\n"
        connection_socket.send(ok_header.encode())

        # send the file content
        for c in output_data:
            connection_socket.send(c.encode())

        connection_socket.send("\r\n".encode())

        print(f"link: http://{server_ip}:{server_port}{file_name}")
        connection_socket.close()

    except IOError:
        error_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connection_socket.send(error_header.encode())

        connection_socket.close()

server_socket.close()
sys.exit()

