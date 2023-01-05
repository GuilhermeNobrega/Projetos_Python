
'''def mostra_valor(p_valor):
    print("Parâmetro recebido:", p_valor)

# Chama a função dentro do main:
if __name__ == '__main__':              # Função principal, atalho: mai + <tab>
    mostra_valor(5)                     	# Chama a função
    mostra_valor(23.8)                  	# Chama a função
    numero = -8
    mostra_valor(numero)                	# Chama a função

def teste_def(oi_def):
    print("Deu certo acho\n")
if __name__ =="__main__":
    teste_def("oia deu certokk")
    teste_def("será que roda msm?")'''


'''def mostralinha():
    print("---------------")
mostralinha()
print("sistema de alunos")
mostralinha()
print("cadastro de funcionários")
mostralinha()
print("erro do sistema")
mostralinha()'''




def título(txt):
    print("-"*30)
    print(txt)
    print("-"*30)


título("  CURSOS GRATUITOS ")  # o que está dentro do título entra em "txt"
título(" OLA MUNDO")


def soma(a , b):
    print("Vamos realizar uma soma")
    s = a + b
    print(f"Soma entre {a} e {b} vale {s} ")

a = int(input("Digite o valor para sua soma"))
b = int(input("Digite o valor para sua soma"))






def contador(*num):
    "for valor in num:"
    tam = len(num)
    print(f"Recebi os valores {num} e contei {tam} números")


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)



def soma(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f"A soma dos valores {valores} vale {s}")
soma(5,2)
soma(2,9,)
