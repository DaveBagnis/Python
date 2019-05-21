import socket as sck

socketClient = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketClient.connect(("127.0.0.1",8080))

socketClient.sendall(b"Sono il client")

data = socketClient.recv(4096)
print(data)

socketClient.close()