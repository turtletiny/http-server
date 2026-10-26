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
server_port = args[2]
file_name = args[3]

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Running at Port: {server_port}, IP: {server_ip}")

while True:
    print("Ready to serve...")

    connection_socket = server_socket.accept()[0]

    try:
        message = connection_socket.recv(1024).decode()
        f = open(file_name)
        outputdata = f.read()
        f.close()
        
        # send HTTP header line
        okHeaderLine = "HTTP/1.1 200 OK\r\n"
        connection_socket.send(okHeaderLine.encode())

        # send the file content
        for c in outputdata:
            connection_socket.send(c.encode())

        connection_socket.send("\r\n".encode())

        print(f"http://{server_ip}:{server_port}{file_name}")
        connection_socket.close()

    except IOError:
        errorHeaderLine = "HTTP/1.1 404 Not Found"

        connection_socket.send(errorHeaderLine.encode())
        connection_socket.send("\r\n".encode())

        connection_socket.close()

server_socket.close()
sys.exit()

