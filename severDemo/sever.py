import socket

Host = ''
Port = 8000

reply = b'Yes'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))

s.listen(3)
while True:
    conn, addr = s.accept()

    request = conn.recv(1024)
    if request==b'stop':
        conn.send(b'ended')
        break
    print('request is :',request)

    if len(request)>10:
        print('so long')
    else:
        print('so short')
    print('request from :', addr)

    conn.send(reply)
conn.close
