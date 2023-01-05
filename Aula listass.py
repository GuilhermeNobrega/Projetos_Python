l1 = list(range(1,10))
print(l1)
x = 0
def soma(x):
    x = int(input("Digite um número:"))
    if x > 10:
        return f"maior que 10, pois x vale {x}"
    elif x == 10:
        return f"igual a 10, pois x vale {x}."
    else:
        return f"menor que 10, pois x vale {x}."
y = soma(x)
print(y)
