'''n = 0
while n < 5: #(enquanto tal condição for verdadeira, execute isso)
    print("-" * 15)
    print(n)
    n = n + 1
print("end", "*" * 15)'''

'''x = 0
while x < 10:
    if x == 3 :
        x = x + 1
        continue
    print(x)
    x = x + 1
print("finish him")'''

'''x = 0
while x < 10:
    if x == 3 :
        x = x + 1
        break #---------- O break finaliza o loop quando ele acha algo pedido para parar
    print(x)
    x = x + 1
print("finish him")'''

print("Calculadora Básica..")
while True:
    n1 = input("Digite um número:")
    n2 = input("Digite outro número:")
    operador = input("Digite um operador:")

    if not n1.isnumeric() or not n2.isnumeric():
        print("Por favor, digite um número.")
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == "+":
        print(n1 + n2)
    elif operador == "-":
        print(n1 - n2)
    elif operador == "*":
        print(n1 * n2)
    elif operador == "/":
        print(n1 / n2)


