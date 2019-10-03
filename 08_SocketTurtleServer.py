from turtle import *
import socket as sck

t = Turtle()
passo = 50
angolo = 90

socketServer = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketServer.bind(("127.0.0.1",8080))

socketServer.listen(1)

conn, address = socketServer.accept()

while True:
    comando = conn.recv(4096)
    print("Comando: " + comando.decode())

    if(comando.decode()=='e'):
        break
    else:
        t.begin_poly()
        if(comando.decode()=='f'):
            t.forward(passo)
        elif(comando.decode()=='b'):
            t.back(passo)
        elif(comando.decode()=='r'):
            t.right(angolo)
            t.forward(passo)
        elif(comando.decode()=='l'):
            t.left(angolo)
            t.forward(passo)
        else:
            print("Comando non valido!")
        x, y = t.pos()
        text = "Coord: " + str(x) + " | " + str(y)
        print(text)
        conn.sendall(text.encode())


t.end_fill()
print("Ho finito")

socketServer.close()