import socket

def sayHey():
    hey_msg = 'Bingo!!!'
    return hey_msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

client_msg = sayHey()

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes(client_msg,"utf-8"))
    clientsocket.close()