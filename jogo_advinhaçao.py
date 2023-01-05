secreto = "perfume"
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print("Você perdeu!!")
        break
    letra = input("Digite uma letra que tenha na palavra secreta:")
    if len(letra) > 1:
        print("Erro.. digite apenas uma letra para o sistema computar..")
        continue
    digitadas.append(letra) # usaremos isso para salvar todas as letras digitadas pelo usuário na lista... por isso o append!!!
    if letra in secreto:
        print(f"Muito bem! a letra  ☞ {letra} ☚ está na palavra secreta..")
    else:
        print(f"Poxa, a letra  ☞ {letra} ☚ não está na palavra secreta..")
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    if secreto_temporario == secreto:
        print(f"Parabéns, você descobriu a palavra secreta!!!! Era {secreto_temporario}")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")
    if letra not in secreto:
        chances -= 1    # chances = chances - 1
    print(f"Você ainda tem {chances} chances..")
    print()
