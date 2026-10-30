from socket import *
import sys
import threading


SERVER_PORT = 6969
SERVER_IP = "192.168.0.133"
MAX_THREADS = 5

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
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
        file_name = message.split()[1]
        f = open(file_name[1:])
        output_data = f.read()
        f.close()

        # send HTTP header line
        ok_header = "HTTP/1.1 200 OK\r\n"
        connection_socket.send(ok_header.encode())

        # send the file content
        for c in output_data:
            connection_socket.send(c.encode())

        connection_socket.send("\r\n".encode())

        print(f"link: http://{SERVER_IP}:{SERVER_PORT}{file_name}")
        connection_socket.close()

    except IOError:
        error_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connection_socket.send(error_header.encode())

        connection_socket.close()

server_socket.close()
sys.exit()






