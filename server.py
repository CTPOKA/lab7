import socket
from random import randrange
from threading import Thread

host = '127.0.0.1'

class TicTacToe:
    d = [[0,0,0],[0,0,0],[0,0,0]]
    c = [' ','X','O']
    t = 2
    def Turn(self, x, y):
        self.t = self.t % 2 + 1
        if (self.d[x][y] == 0):
            self.d[x][y] = self.t
            if (self.d[x][(y+1)%3] == self.d[x][(y+2)%3] == self.t or self.d[(x+1)%3][y] == self.d[(x+2)%3][y] == self.t or self.d[0][0] == self.d[1][1] == self.d[2][2] !=0 or self.d[0][2] == self.d[1][1] == self.d[2][0] != 0):
                return self.t
            return 0
        else: return -1

    def Print(self):
        str = "     1   2   3  \n   ╔═══╦═══╦═══╗\n"
        str += f" 1 ║ {self.c[self.d[0][0]]} ║ {self.c[self.d[1][0]]} ║ {self.c[self.d[2][0]]} ║\n   ╠═══╬═══╬═══╣\n"
        str += f" 2 ║ {self.c[self.d[0][1]]} ║ {self.c[self.d[1][1]]} ║ {self.c[self.d[2][1]]} ║\n   ╠═══╬═══╬═══╣\n"
        str += f" 3 ║ {self.c[self.d[0][2]]} ║ {self.c[self.d[1][2]]} ║ {self.c[self.d[2][2]]} ║\n   ╚═══╩═══╩═══╝\n"
        return str


def TCP():
    conn, addr = stcp.accept()
    while True:
        data = conn.recv(1024)
        y, x = map(int, data.decode().split(' '))
        print(x,y)
        res = game.Turn(x-1, y-1)
        if (res == -1 or x > 3 or x < 1 or y > 3 or y < 1):
            conn.send(f"Ошибка, не коректно введены данные\n".encode())
        print(f"Клиент: Сделан ход X {y} {x} ")
        str = f"Вы: Сделан ход X {y} {x}\n" + game.Print()
        conn.send(str.encode())
        print(game.Print())
        if (res == 1):
            conn.send("Вы победили!".encode())
            print("Вы проиграли...")
            break
        print("\nВаш ход!")
        y, x = map(int, input().split(' '))
        print(f"Вы: Сделан ход O {y} {x} ")
        res = game.Turn(x-1, y-1)
        if (res == -1 or x > 3 or x < 1 or y > 3 or y < 1):
            print("Ошибка, не коректно введены данные")
        str = f"Сервер: Сделан ход X {y} {x}\n" + game.Print()
        conn.send(str.encode())
        print(game.Print())
        if (res == 2):
            print("Вы победили!")
            conn.send("Вы проиграли...".encode())
            break

def UDP():
    while True:
        data, addr = sudp.recvfrom(1024)
        y, x = map(int, data.decode().split(' '))
        res = game.Turn(x-1, y-1)
        if (res == -1 or x > 3 or x < 1 or y > 3 or y < 1):
            conn.send(f"Ошибка, не коректно введены данные\n".encode())
        print(f"Клиент: Сделан ход X {y} {x} ")
        str = f"Вы: Сделан ход X {y} {x}\n" + game.Print()
        sudp.sendto(str.encode(), addr)
        print(game.Print())
        if (res == 1):
            conn.send("Вы победили!".encode())
            print("Вы проиграли...")
            break
        print("\nВаш ход!")
        y, x = map(int, input().split(' '))
        print(f"Вы: Сделан ход O {y} {x} ")
        res = game.Turn(x-1, y-1)
        if (res == -1 or x > 3 or x < 1 or y > 3 or y < 1):
            print("Ошибка, не коректно введены данные")
        str = f"Сервер: Сделан ход X {y} {x}\n" + game.Print()
        sudp.sendto(str.encode(), addr)
        print(game.Print())
        if (res == 2):
            print("Вы победили!")
            conn.send("Вы проиграли...".encode())
            break


if __name__ == '__main__':
    game = TicTacToe()
    print("Сервер\nВыберите протокол: 1-TCP  2-UDP")
    answ = input()
    if (answ == "1"):
        stcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stcp.bind((host, 8888))
        stcp.listen()
        t1 = Thread(target=TCP)
        t1.start()
        t1.join()
    elif (answ == "2"):
        sudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sudp.bind((host, 9090))
        t2 = Thread(target=UDP)
        t2.start()
        t2.join()
