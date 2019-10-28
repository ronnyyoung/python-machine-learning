import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 在udp的client中可以使用connect，来绑定要发送消息的目标地址
# 这样在后续发送时，可以直接使用send而不是sendto
s.connect((('127.0.0.1', 9856)))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.close()