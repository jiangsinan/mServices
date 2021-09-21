import socket

socket = socket.socket()

socket.connect(('127.0.0.1',8010))

msg = socket.recv(4096)
print('Server:',msg.decode('utf-8'))

socket.send('您好 想听歌'.encode('utf-8'))

socket.close()

