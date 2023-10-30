import socket

PORT = 8020
SERVER = "172.16.202.152"
ADDR = (SERVER,PORT)
DISCONNECT="!DISCON"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode()

    client.send(message)
    print(client.recv(2048).decode())

#enter 1 to send msg ,Anything other than 1 will exit you from server
while True:
    n=input()
    if n=="1":
        send(input())
    elif n=="2":
        x=int(input())
        for i in range(x):
            send(input())
    else:
        send(DISCONNECT)
        break