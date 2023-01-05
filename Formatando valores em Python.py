
""" Formatando valores com modificadores -- 5
:s  ---texto ( strings)
:d --- inteiros (int)
:f ---- pontos flutuantes ( float)
:.(número de casas decimais)f - quantidade de casas decimais
:(caractere) (> ou < ou ^) (quantidade) (tipo - s , d ou f)
 > ---- esquerda
 < ----- direita
 ^ centro """
'''n1 = 4
n2 = 2
divisao = n1 / n2
print(f"{divisao:.0f}")'''

n1 = 1
print(f"{n1:0>10}")
# resulta em 0000000001
n2 = 1150
print(f"{n2:0^10}")
nome = "Guilherme"
print(nome.upper()) # Maiúsculo
print(nome.lower()) # Minúsculo
print(nome.title()) # Primeiras letras maisculas
print(nome)
