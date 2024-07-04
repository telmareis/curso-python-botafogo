# ler o nome do usuario
nome = input("Qual o nome? ").strip().title()

primeiro, sobrenome = nome.split(" ")

# exibir uma mensagem na tela de saudação
print(f"Olá, {nome}")
print(sobrenome)
