print("********************")
print("Olá, Bem vindo!")
print("********************")

numero_secreto = "42"
total_de_tentativas = 5

while (total_de_tentativas > 0):
    print("Tentativas:", total_de_tentativas)

    chute = input("Digite o seu número: ")

    print("Você digitou:", chute)

    acertou  = chute == numero_secreto
    maior    = chute >  numero_secreto
    menor    = chute <  numero_secreto

    if (acertou):
        print("Parabéns!! Você acertou o número secreto.")

    else:
        if(maior):
            print("Você errou! o Seu chute foi alto demais.")
        elif(menor):
            print("Você errou! Seu chute foi baixo demais.")

    total_de_tentativas = total_de_tentativas - 1

print("Fim do Jogo!")
