#(1)
'''def saudação(nome):
    print("olá",nom,"seja muito bem vindo")
nom = str(input("Digite seu nome:"))
saudação(nom)'''
#--------------------------------------
#(2)
'''def soma(n1,n2,n3):
    s = n1 + n2 + n3
    print(s)
    OU return s
x = float(input("PRIMEIRO NÚMERO:"))
y = float(input("SEGUNDO NÚMERO:"))
z = float(input("TERCEIRO NÚMERO:"))
soma(x,y,z)'''
#-------------------------------------
#(3)
def strange(n1,n2):
    print('')
x = float(input("Primeiro valor:"))
y = int(input("Porcentagem que deseja:%"))
print(f"faremos a soma do valor {x} com a porcentagem {y}%")
conta = (y/100) * x + x
print(conta,"%")
#strange(x,y)

# ou def strange(n1,n2):
#     return (y/100) * x + x
#
# x = float(input("Primeiro valor:"))
# y = int(input("Porcentagem que deseja:"))
# print(f"faremos a soma do valor {x} com a porcentagem {y}%")
# print(strange(x,y)) printa o valor do retorno

#------------------------------------
#(4)

def loucura(n1):
    if n1 % 3 == 0 and x % 5 == 0:
        return f'fizzbuzz, {n1} é divisível por 3 e 5'
    elif n1 % 5 == 0:
        return f'buzz, {n1} é divisível por 5'
    elif n1 % 3 == 0:
        return f'fizz, {n1} é divisível por 3'
    return n1
#return ==  jogar para fora função...
x = int(input("Digite o seu valor:"))
print(loucura(x))