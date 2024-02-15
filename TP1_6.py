# TP1.6
# Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

import random

def Main():
    numRandom = SelecionarNumero()
    PedeNumero(numRandom)

def SelecionarNumero():
    numSelecionado = random.randint(0, 9)
    print(f"O número gerado foi {numSelecionado}\n")
    return numSelecionado

def PedeNumero(numRandom):
    counter = 3
    while counter > 0:
        print(f"Você tem {counter} chances...")
        numEscolhido = int(input("Escolha um número: "))
        if numEscolhido == numRandom:
            print("Parabéns! você acertou!\n")
            break
        else:
            if numEscolhido > numRandom:
                print("Chute mais baixo.\n")
                counter -= 1
            else:
                print("Chute mais alto.\n")
                counter -= 1
    print("Game Over!")

Main()