personagens = ["Frodo", "Sam", "Legolas", "Gandalf", "Ginly", "Smeagol", "Bilbo"]

print(personagens[2])

print(personagens)

print("Lista fixa...")
for i in range(4):
    print("Nome:",personagens[i], end="\n")

print("Lista dinâmica...")
for personagem in personagens:
    print("Nome:",personagem)