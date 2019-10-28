import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9856))
while True:
    data, addr = s.recvfrom(1024)
    print('Received data from %s:%s' % addr)
    s.sendto(b'hello: %s' % data, addr)
s.close()