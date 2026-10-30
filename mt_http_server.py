from socket import *
import sys
import threading


SERVER_PORT = 6969
SERVER_IP = "192.168.0.133"
MAX_THREADS = 5

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

def init_thread():
    (connection_socket, addr) = server_socket.accept()

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

threads: list[threading.Thread] = []

count = 1

while True:
    print(count)
    count += 1

    thread = threading.Thread(target=init_thread)
    thread.start()
    thread.join()


server_socket.close()
sys.exit()






