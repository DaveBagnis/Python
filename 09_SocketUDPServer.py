import socket as sck

HOST = "0.0.0.0"
PORT = 5000

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
    data, address = s.recvfrom(4096)
    print("ricevuto --> " + str(data) + "da" + str(address))

    if(str(data) == "end"):
        break

    text = input("Inserisci risposta: ")
    s.sendto(text.encode(),address)

s.close()