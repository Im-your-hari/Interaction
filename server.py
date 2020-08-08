import socket

s = socket.socket()

s.bind(('localhost',1234))

s.listen(5)

while True:
    c,addr = s.accept()
    print("Connected with ",addr)
    msg = input('->')
    c.send(bytes(msg,'utf-8'))
