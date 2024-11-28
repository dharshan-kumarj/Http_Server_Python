import socket
import time

Port = 8080
Host = '127.0.0.1'

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_socket.bind((Host,Port))
server_socket.listen(5)
print(f"Server is listening on {Host}:{Port}")

while True :
    client_socket,client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    print(request)
    headers = request.split('\n')

    first_headers_components = headers[0].split()
 
    http_method=first_headers_components[0]
    http_path=first_headers_components[1]
    
    if http_method == 'GET':
        if http_path == '/' :
            fin = open('index.html')
            content = fin.read()
            fin.close()

            response = 'HTTP/1.1 200 OK \n\n' + content
            client_socket.sendall(response.encode())
            client_socket.close()
        elif http_path == '/test':
            fin = open('test.json')
            content = fin.read()
            fin.close()

            response = 'HTTP/1.1 200 OK \n\n' + content
            client_socket.sendall(response.encode())
            client_socket.close()

    else :
        response = 'HTTP/1.1 405 Method Not Allowed \n\n Allow only GET Method'
        client_socket.sendall(response.encode())
        client_socket.close()

    

