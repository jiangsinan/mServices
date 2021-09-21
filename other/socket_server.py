import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',8010))

server.listen()

print('服务端已启动...')
client,address = server.accept()
print('%s 已连接'%address[0])

client.send('您好，我是小爱同学'.encode('utf-8'))

msg = client.recv(4096)
print(address,'说',msg.decode())

client.close()
server.close()