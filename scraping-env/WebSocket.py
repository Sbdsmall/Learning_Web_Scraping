import socket
# Simple WebSocket-like connection using raw sockets
host = 'www.google.com'
port = 80
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
client_socket.connect(server_address)

request_header = b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
client_socket.sendall(request_header)

response = ''
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data.decode('utf-8')

print(response)
client_socket.close()