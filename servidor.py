import socket

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        numbers = [float(num) for num in data.decode().strip().split()]
        result = None
        if numbers[0] == 1:
            result = sum(numbers[1:])
        elif numbers[0] == 2:
            result = numbers[1]
            for num in numbers[2:]:
                result -= num
        elif numbers[0] == 3:
            result = 1
            for num in numbers[1:]:
                result *= num
        elif numbers[0] == 4:
            result = numbers[1]
            for num in numbers[2:]:
                result /= num
        conn.sendall(str(result).encode())
    print(f"Conexão com {addr} fechada")

def main():
    HOST = ''  # Todas as interfaces disponíveis
    PORT = 15000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Servidor ouvindo na porta {PORT}")
        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)

if __name__ == "__main__":
    main()
