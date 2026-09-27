

#TPC2 "Adivinha o número

import random
#def adivinha_numero():
print("=== Adivinha o número ===")
print("1 - Computador pensa num número (0 a 100) e o utilizador adivinha")
print("2- Utilizador pensa num número (0 a 100) e o computador adivinha")

modalidade = input("Escolhe a modalidade (1 ou 2):")
    



if modalidade == "1":
    secreto = random.randint (0,100)
    tentativas = 0
    print("\nO computador pensou num número entre 0 e 100")

    while True:
        palpite= int(input("Qual é o seu palpite? "))
        tentativas += 1

        if palpite ==secreto:
            print("Acertou")
            print(f"Número de tentativas utilizadas: {tentativas}")
            break
        elif palpite < secreto:
            print ("O número que pensei é maior")
        else:
            print("O número que pensei é menor")

elif modalidade == "2":
    baixo= 0
    alto=100
    tentativas = 0
    print("\nPensa num número entre 0 e 100 e responde às perguntas do computador.")

    while baixo <= alto:
        palpite = (baixo + alto) // 2
        tentativas +=1

        print (f"\nTentativa {tentativas}: O número em que pensou é {palpite}?")
        print ("1-Acertou")
        print("2- o número que pensei é maior")
        print("3- o número que pensei é menor")

        resposta = input ("Escolhe (1,2 ou 3):").strip()

        if resposta == "1":
            print("Acertou")
            print(f"Número de tentativas utilizadas: {tentativas}")
            break
        elif resposta == "2":
            baixo= palpite + 1
        elif resposta == "3":
            alto = palpite -1
        else:
            print ("Resposta incorreta. Tente novamente.")
            tentativas -=1

    else:
        print("modalidade incorreta: Escolha 1 ou 2.")
