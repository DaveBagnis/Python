import socket as sck

socketServer = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

socketServer.bind(("127.0.0.1",8080))

socketServer.listen(1)

conn, address = socketServer.accept()

data = conn.recv(4096)
print(data)

conn.sendall(data)

socketServer.close()