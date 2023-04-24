import socket

Host = '127.0.0.1'
Port = 8000

request = input('>').encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

s.sendall(request)
reply = s.recv(1024)

print('reply is :', reply)
s.close()
