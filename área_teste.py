'''def strange(n1,n2):
    print(f"{n1} + {n2}% =")
    return (y/100) * x + x

x = float(input("Primeiro valor:"))
y = int(input("Porcentagem que deseja:%"))
print(f"faremos a soma do valor {x} com a porcentagem {y}%")
print(strange(x,y))'''

'''variavel = "valor"
def funcao():
    print(variavel)
def funcao2():
    # global variavel
    variavel = "outro2"
    print(variavel)
funcao()
funcao2()
print(variavel)'''
#-------------
variavel = "valor"
def funcao():
    outra_variavel = "valor"
    return outra_variavel
def funcao2(oi):
    # global variavel
    print(oi,"oi")
var = funcao()
funcao2(var)
def soma(x,y):
    print(f"{x} + {y} ==")
    return x + y
print(soma(2,1))