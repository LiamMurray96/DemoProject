import socket

# Creazione di un socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connesione al server socket
client_socket.connect(('localhost', 3000))

while True:
    move = input("inserisci movimento (ex. UP/DOWN/LEFT/RIGHT): ")
    client_socket.sendall(move.encode())