import socket


def menu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")


def main():
    HOST = 'localhost'  # Endereço IP ou nome de host do servidor
    PORT = 15000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao servidor.")
        while True:
            menu()
            choice = input("Escolha uma opção: ")
            if choice == '5':
                break
            numbers = input("Digite os números separados por espaço: ")
            data = f"{choice} {numbers}\n"
            s.sendall(data.encode())
            result = s.recv(1024).decode()
            print("Resultado:", result)


if __name__ == "__main__":
    main()
