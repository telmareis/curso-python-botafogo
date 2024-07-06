nome = input("Digite o personagem ")

match nome:
    case "Frodo" | "Sam":
        print("Hobbit")
    case "Aragorn":
        print("Homem")
    case "Gandalf":
        print("Mago")
    case _:
        print("Quem???")

