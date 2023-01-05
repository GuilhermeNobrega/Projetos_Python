print("Exercício (1)")
n1 = input('Digite um número inteiro: ')
if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0:
        print(f"O número {n1} é par")
    else:
        print(f" O número {n1} é ímpar")
else:
    print("Erro. Digite um número inteiro")




'''print("Exercício (2)")
data = int(input("Digite o horário atual:"))
if data >= 0 and data <= 11:
    print("Bom dia!!!!!!!!!!!!")
elif data >= 12 and data <= 17:
    print("Boa tarde!!!!!!!!!!")
elif data >= 18 and data <= 23:
    print("Boa noite!!!!!!!!!")'''






#__________________________________________________________________
'''print("Exercício (3)")
nome = str(input("Digite seu primeiro nome:"))
quantos = len(nome)
if quantos <= 4:
    print("Seu nome é curto.")
elif quantos >= 5 and quantos <= 6:
    print("O seu nome é normal.")
elif quantos > 6:
    print("Seu nome é muito grande.")'''
