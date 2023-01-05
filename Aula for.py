#Função range(start=0, stop, step=1)
#for c in range(20,0,-1):
   # print(c)
n1 = int(input("Digite o valor de sua tabuada:"))
for c in range(0,11):
    print("/////////////")
    print(f"{c} x {n1} = {c * n1}")
print("FIM")

#continue - pula para o próximo laço
#break - termina o laço

'''texto = "Python"
nova_string = ""
for letra in texto:
    if letra == "t":
        #continue
        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
        #break
    else:
        nova_string +=letra
print(nova_string)'''
nome = "Guilherme"
for nomezao in nome:
    print(nomezao)