import socket

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Cria o socket do cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor
    s.connect((HOST, PORT))
    # Envia dados ao servidor
    s.sendall(b'Hello, servidor!')
    # Recebe a resposta do servidor
    data = s.recv(1024)

print('Resposta do servidor:', data.decode())
