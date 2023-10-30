import socket
import threading

PORT = 8020
SYSTEM_NAME = socket.gethostname()
SERVER = socket.gethostbyname(SYSTEM_NAME)
ADDR = (SERVER,PORT)
DISCONNECT = "!DISCON"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn,addr):
    (ip_addr, port) = addr
    print("\nNEW CONNECTION ESTABLISHED")
    print("Connection details :")
    print("IP_ADDRESS : ",ip_addr)
    print("PORT : ",port,"\n")

    while True:
        msg = conn.recv(4096).decode()
        if msg:
            if msg == DISCONNECT:
                break
            print(addr ,"sent a msg : ",msg)
            conn.send("Msg received".encode())
    print(addr ,"Disconnected")
    conn.close()
    pass

def start():
    server.listen()
    print("Server is listening on \nSYSTEM NAME : ",SYSTEM_NAME,"\nIP_address : ",SERVER,"\nPORT : ",PORT)
    while True:
        conn,addr = server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        try :
            print("\nACTIVE CONNECTIONS : ",threading.activeCount()-1,"\n")
        except :
            print("something went wrong ,connection lost")
print("server is starting...")
start()
