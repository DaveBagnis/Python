import socket as sck

SERV = "127.0.0.1"
PORT = 5000

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)

while True:
    testo = input("Inserisci il messaggio: ")
    s.sendto(testo.encode(), (SERV, PORT))

    if(str(testo) == "end"):
        break

    data, server = s.recvfrom(4096)
    print("ricevuto --> " + str(data) + "da " + str(server)

s.close()