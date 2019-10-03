import socket as sck

socketClient = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketClient.connect(("127.0.0.1",8080))

while True:    
    text = input("Inserisci il mex: ")   
    socketClient.sendall(text.encode())
    if(text=='e'):
        break
    elif(text!='f' and text!='b' and text!='l' and text!='r'):
        print("Comando non valido!")

    data = socketClient.recv(4096)
    pezzi = data.decode().split()
    x = float(pezzi[1])
    y = float(pezzi[3])
    print("X = " + str(x) + " | Y = " + str(y))

socketClient.close()