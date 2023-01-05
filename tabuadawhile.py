while True:
    print("Se desejar sair, digite (-1)")
    x = int(input("Digite o valor de tabuada que você deseja:"))
    if x == -1:
        print("Acabou.")
        break
    else:
        for c in range(0, 11):
            s = x * c
            print(f"{x} x {c} =  {s}")
# print("Deseja continuar?")





