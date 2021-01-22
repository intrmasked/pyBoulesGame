
#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the Boules Game!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)            #used to decode the message

        
clients = {}                    #array to store the clients connected to the server
addresses = {}                  #ip addresses of the clients connected

HOST = ''                       #host of the server
PORT = 33000                    #to define the port
BUFSIZ = 1024
ADDR = (HOST, PORT)             #puts host and port in one variable

SERVER = socket(AF_INET, SOCK_STREAM)   #This call results in a stream socket with the TCP protocol providing the underlying communication
SERVER.bind(ADDR)               # used to connect to the host and port

if __name__ == "__main__":          # block to allow or prevent parts of code from being run when the modules are imported.
    SERVER.listen(5)                       # to accept incoming connections
    print("Waiting for connection...")      #shows that in the terminal that the code has started
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)      #defines the thread and its target
    ACCEPT_THREAD.start()           #to start the threading process
    ACCEPT_THREAD.join()            # used to let the main thread finish before starting another thread
    SERVER.close()                  # to close a thread