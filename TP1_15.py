# TP1.15
# Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

import time

def Main():
    print("Bem-vindo à História Interativa!")
    time.sleep(1)

    print("\nVocê está em uma floresta misteriosa.")
    time.sleep(1)

    escolha1 = input("\nVocê quer seguir pela trilha à esquerda ou pela trilha à direita? (esquerda/direita): ").lower()
    
    if escolha1 == "esquerda":
        print("\nVocê encontra uma clareira tranquila.")
        time.sleep(1)
        print("Na clareira, há uma cabana abandonada e uma lagoa serena.")
        time.sleep(1)

        escolha2 = input("\nVocê deseja explorar a cabana ou dar um mergulho na lagoa? (cabana/lagoa): ").lower()

        if escolha2 == "cabana":
            print("\nDentro da cabana, você encontra um mapa do tesouro antigo!")
            time.sleep(1)
            print("Parabéns! Você descobriu um tesouro escondido.")
        elif escolha2 == "lagoa":
            print("\nVocê nada na lagoa e encontra uma passagem subaquática secreta.")
            time.sleep(1)
            print("Ao explorar a passagem, você descobre um portal para um mundo mágico!")
        else:
            print("\nEscolha inválida. Você se perde na floresta.")

    elif escolha1 == "direita":
        print("\nVocê segue por um caminho íngreme cheio de pedras.")
        time.sleep(1)
        print("No final do caminho, há uma ponte que leva a uma montanha alta.")
        time.sleep(1)

        escolha3 = input("\nVocê quer atravessar a ponte ou escalar a montanha? (ponte/montanha): ").lower()

        if escolha3 == "ponte":
            print("\nA ponte balança, mas você a atravessa com sucesso.")
            time.sleep(1)
            print("Do outro lado, você encontra uma aldeia amigável.")
        elif escolha3 == "montanha":
            print("\nVocê escala a montanha e descobre uma caverna misteriosa.")
            time.sleep(1)
            print("Dentro da caverna, há cristais brilhantes que concedem poderes mágicos!")
        else:
            print("\nEscolha inválida. Você se perde na floresta.")

    else:
        print("\nEscolha inválida. Você se perde na floresta.")

Main()
