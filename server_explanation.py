import socket

# Creazione socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind indirizzo IP e porta
server_socket.bind(('localhost',3000))
# Accetta massimo 2 connesioni simultaneamente
server_socket.listen(2)

clients = []

while True:
        # accettiamo una nuova connesione
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"connessa {addr}")
