n = int(input("Digite o número de convidados"))
cont = 0
lista = []
while cont <=n:
    nome = str(input("Digite o nome do convidado #" + str(cont)))
    lista.append(nome)
    cont = cont + 1
print(lista)