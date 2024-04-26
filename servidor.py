import socket

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta para escutar conexões

# Cria o socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Liga o socket ao endereço e porta especificados
    s.bind((HOST, PORT))
    # Fica escutando por conexões
    s.listen()
    print("Servidor esperando por conexões...")
    # Aceita a conexão
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            # Recebe os dados do cliente
            data = conn.recv(1024)
            if not data:
                break
            # Imprime os dados recebidos
            print('Dados recebidos:', data.decode())
            # Envia uma resposta ao cliente
            conn.sendall(b'Recebido com sucesso!')
