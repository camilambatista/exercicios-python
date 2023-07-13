print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1


while rodada <= total_de_tentativas:
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto

    if acertou:
        print("Você acertou!")
        break
    elif maior:
        print("Você errou! Você chutou pra cima!")
    else:
        print("Você errou! Você chutou pra baixo!")

    print("Fim do jogo!")
    rodada += 1








