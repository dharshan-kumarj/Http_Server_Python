import socket
import time

Port = 8080
Host = '127.0.0.1'

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.setblocking(False)

server_socket.bind((Host,Port))
server_socket.listen(5)
print(f"Server is listening on {Host}:{Port}")

while True :
    try:
        client_socket,client_address = server_socket.accept()
        print(f"Client_socket {client_socket} : Client_ADdress{client_address}")
    except:
        time.sleep(2)
        continue
