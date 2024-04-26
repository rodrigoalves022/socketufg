import socket


def manipular_conexao_cliente(cliente_soquete):
    while True:
        # Recebe a mensagem do cliente e converte para uma sting
        solicitacao = cliente_soquete.recv(1024).decode()
        if not solicitacao:
            break

        # Separa a mensagem em partes, como [soma, 1, 2, 3]
        partes = solicitacao.split()
        # Seleciona a Operação
        operacao = partes[0]
        # Seleciona os numeros e converte
        numeros = list(map(float, partes[1:]))

        # Executa a operação solicitada
        if operacao == 'soma':
            resultado = sum(numeros)

        elif operacao == 'subtracao':
            resultado = numeros[0] - sum(numeros[1:])

        elif operacao == 'multiplicacao':
            resultado = 1
            for num in numeros:
                resultado *= num

        elif operacao == 'divisao':
            resultado = numeros[0]
            for num in numeros[1:]:
                if num != 0:
                    resultado /= num
                else:
                    resultado = "Erro: Divisão por zero"
                    break

        else:
            resultado = "Erro: Operação inválida"

        # Envia o resultado de volta para o cliente
        cliente_soquete.sendall(str(resultado).encode())

    # Fecha a conexão com o cliente
    cliente_soquete.close()


def main():
    # Configurações do servidor
    ip = '10.62.102.100'
    porta = 15000

    # Cria o socket do servidor, passando o tipo de endereço (IPV4) e o Protocolo TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_soquete:
        # Liga o socket ao IP e porta especificos
        servidor_soquete.bind((ip, porta))
        # Fica escutando por conexões
        servidor_soquete.listen()

        print(f"Servidor {ip} esperando por conexões na porta {porta}...")

        while True:
            # Aceita a conexão
            cliente_soquete, addr = servidor_soquete.accept()
            print(f"Conexão recebida de {addr[0]}:{addr[1]}")

            # Lida com a conexão do cliente em uma nova thread
            manipular_conexao_cliente(cliente_soquete)


if __name__ == "__main__":
    main()
