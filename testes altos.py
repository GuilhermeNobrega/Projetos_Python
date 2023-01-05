produtos = ["ABC123" , "abd012" , " ABS111" , "AbB222"]
#texto = "abd012"
#texto = texto.upper()
#texto = texto.strip()
#print(texto)
#queremos arrumar essas valores na lista.. temos que ter isso na função!
def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto
#texto = " abd012 "
#texto = tratar_texto(texto)
#print(texto)
for i, produto in enumerate(produtos): #para cada produto dentro da lista de produtos
    produtos[i] = tratar_texto(produto)
print(produtos)
def mensagem():
    print("olá mundo, sou novo e aprendiz em python")
    #return mensagem()
mensagem()
x = 10
y = 15
def soma(x,y):
    return x + y #usaremos pois atribuiremos uma variável lá embaixo, então ele precisa retornar algo.. r = soma(x,y)   print(r)
r = soma(x,y)
print(r)
valores = [1,2,3,4,5]
def quadrado(valores):
    quadrados = []
    for x in valores:
        quadrados.append(x**2)
    return quadrados
resultados = quadrado(valores) # para chamar uma função precisamos armazenar os resultados
for y in resultados:
    print(y)