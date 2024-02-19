# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client



import socket
import threading

# HOST = "192.168.1.10"
# HOST = "178.204.180.19" #PUBLIC
# HOST = socket.g
# HOST = "127.0.0.1"
print(socket.gethostbyname(socket.gethostname()))
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        print("server broadcast")
        print(type(message))
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")  #receive a message from the client
            print("RECEIVING A MESSAGE FROM THE CLIENT")
            index = clients.index(client)
            broadcast(f"{nicknames[index]}: {message}\n".encode())
        except  Exception as e:
            print(e)
            # index = clients.index(client) 
            # clients.remove(client)
            # client.close() #closing the socket/connection
            # nicknames.remove(nicknames[index])
            break

def receive():
    while True:
        client, address = server.accept()  #client is a socket repr new connection 
        # print(f"{client} connected with {str(address)}")
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        print(f"Nickname: {nickname}")
        clients.append(client)
        nicknames.append(nickname)
        # print(f"the nickname is {nickname}")
        broadcast(f"{nickname} joined the chat\n".encode("utf-8"))
        # client.send("connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

print("server running")
receive() 