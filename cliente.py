import socket
import os


def limpar_prompt():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print("Operações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Encerrar programa")


def enviar_solicitacao(operacao, numeros):
    ip = '10.62.102.100'
    porta = 15000
    # Cria o socket do cliente, passando o tipo de endereço (IPV4) e o Protocolo TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_soquete:
        # Conecta ao servidor
        cliente_soquete.connect((ip, porta))

        # Coloca tudo em uma string
        solicitacao = operacao + " " + " ".join(map(str, numeros))

        # Envia a solicitação para o servidor
        cliente_soquete.sendall(solicitacao.encode())

        # Recebe a resposta do servidor
        resposta = cliente_soquete.recv(1024).decode()
        print("Resposta do servidor:", resposta)


def validar_escolha(escolha):
    limpar_prompt()
    if not (isinstance(escolha, int) and 1 <= escolha <= 5):
        print('Digite um número inteiro no intervalo de 1 a 5.')
        print()
        return True


def obter_numeros():
    # Separa os numeros, transforma em float e mapeia para a lista
    return list(map(float,
                    input("Digite os números separados por espaço: ").split()
                    )
                )


def main():
    while True:

        menu()
        escolha = int(input("Escolha uma operação (1-5): "))

        if validar_escolha(escolha):
            continue

        if escolha == 1:
            numeros = obter_numeros()
            enviar_solicitacao('soma', numeros)

        elif escolha == 2:
            numeros = obter_numeros()
            enviar_solicitacao('subtracao', numeros)

        elif escolha == 3:
            numeros = obter_numeros()
            enviar_solicitacao('multiplicacao', numeros)

        elif escolha == 4:
            numeros = obter_numeros()
            enviar_solicitacao('divisao', numeros)

        elif escolha == 5:
            print("Encerrando o programa...")
            break


if __name__ == "__main__":
    main()
