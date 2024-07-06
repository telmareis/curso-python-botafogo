def isPar(numero):
    return numero % 2 == 0

def main():
    # ler um número
    valor = int(input("Digite um número "))

    # verificar se é par ou impar
    if isPar(valor):
        print("Par")
    else:
        print("Ímpar")

main()