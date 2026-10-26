from socket import *
import sys

SERVER_PORT = 6969
SERVER_IP = "192.168.0.133"

# Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_IP, SERVER_PORT))
serverSocket.listen(1)

print(f"Running at Port: {SERVER_PORT}, IP: {SERVER_IP}")

while True:
    #Establish a connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        
        # send HTTP header line
        okHeaderLine = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(okHeaderLine.encode())

        # send the file content
        for c in outputdata:
            connectionSocket.send(c.encode())

        connectionSocket.send("\r\n".encode())

        print(f"http://{SERVER_IP}:{SERVER_PORT}{filename}")
        connectionSocket.close()

    except IOError:
        errorHeaderLine = "HTTP/1.1 404 Not Found"

        connectionSocket.send(errorHeaderLine.encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()

