import socket
import threading

def echo(sock, addr):
    print('Accpet connection from %s:%s' % addr)
    sock.send(b'Hello')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(data)
    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9856))
s.listen(10)
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=echo,args=(conn, addr))
    t.start()
