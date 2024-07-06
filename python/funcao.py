def exibirMensagem():
    print("Sou uma função")

def exibirSaudacao(nome, total):
    print("Olá,",nome)
    print("O total da soma é",total)

def somar(valor1, valor2):
    total = valor1 + valor2
    return total

def main():
    soma = somar(6, 9) 
    exibirMensagem()
    print(soma)
    exibirSaudacao("Antônio José", soma)

main()