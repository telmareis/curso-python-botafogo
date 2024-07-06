x = int(input("Digite o valor de x "))
y = int(input("Digite o valor de y "))

if x < y:
    print("x é menor do que y")
elif x > y:
    print("x é maior do que y")
else:
    print("x e y são iguais")

if x < y or x > y:
    print("x e y são diferentes")

if x == y and y == x:
    print("x e y são iguais")