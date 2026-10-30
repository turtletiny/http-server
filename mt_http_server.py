from socket import *
import sys
import threading

DEFAULT_IP = "192.168.0.133"
MAX_PORT = 65535
MAX_THREADS = 5

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
server_socket.listen()

threads: list[threading.Thread] = []
sockets: list[socket] = []

def init_thread(idx: int):
    sockets.append(server_socket.accept()[0])


# init threads
for i in range(MAX_THREADS):
    thread = threading.Thread(target=init_thread, args=(i,))
    threads.append(thread)

threads_used = 0

while True:

    print(f"Sockets used: {threads_used}/{MAX_THREADS}")

    (connection_socket, port) = server_socket.accept()

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






