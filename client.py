import socket

c = socket.socket()

c.connect(('localhost',1234))

while True:
    msg = input(">>")
    c.send(bytes(msg,'utf-8'))
    print(c.recv(1024).decode)
