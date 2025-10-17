import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
s.bind(('127.0.0.1', 8888))
print("UDP сервер слушает порт 8888...")

try:
    
    while 1:
     data, addr = s.recvfrom(1024)
     print("Сообщение от {}: {}".format(addr, data.decode('utf-8')))
except KeyboardInterrupt:
    print("\nОтключение сервера...")

finally:
    s.close()
