from socket import *
import sys
import threading
import time


SERVER_PORT = 6969
SERVER_IP = "192.168.0.133"

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

def serve_client(connection_socket: socket):
    time.sleep(3)

    try:
        message = connection_socket.recv(1024).decode()
        file_name = message.split()[1]
        f = open(file_name[1:])
        output_data = f.read()
        f.close()

        ok_header = "HTTP/1.1 200 OK\r\n"
        response = ok_header + output_data + "\r\n"
        connection_socket.send(response.encode())

        print(f"link: http://{SERVER_IP}:{SERVER_PORT}{file_name}")
        connection_socket.close()

    except IOError:
        error_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connection_socket.send(error_header.encode())

        connection_socket.close()


# main loop
client_count = 1
while True:
    (connection_socket, _addr) = server_socket.accept()

    thread = threading.Thread(target=serve_client, args=(connection_socket,))
    thread.start()

    print(client_count)
    client_count += 1


server_socket.close()
sys.exit()






