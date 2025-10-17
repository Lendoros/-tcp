import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("Введите сообщение ('exit' для выхода): ")
    s.sendto(msg.encode('utf-8'), ('127.0.0.1', 8888))
    if msg == 'exit':
        break
s.close()

