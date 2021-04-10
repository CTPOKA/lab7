import socket
from threading import Thread

host = '127.0.0.1'

def TCP():
    while True:
        print("\nВаш ход!")
        stcp.send(input().encode())
        data = stcp.recv(1024)
        print(data.decode())
        data = stcp.recv(1024)
        print(data.decode())
        if (data.decode() == "Вы победили!"):
            break


def UDP():
    while True:
        print("\nВаш ход!")
        sudp.sendto(input().encode(), (host, 9090))
        data = sudp.recv(1024)
        print(data.decode())
        data = sudp.recv(1024)
        print(data.decode())
        if (data.decode() == "Вы победили!"):
            break


if __name__ == '__main__':
    print("Клиент\nВыберите протокол: 1-TCP  2-UDP")
    answ = input()
    if (answ == "1"):
        stcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stcp.connect((host, 8888))
        t1 = Thread(target=TCP)
        t1.start()
        t1.join()
    elif (answ == "2"):
        sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sudp.connect((host, 9090))
        t2 = Thread(target=UDP)
        t2.start()
        t2.join()
