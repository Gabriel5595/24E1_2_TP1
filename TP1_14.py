# TP1.14
# Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

def Main():
    
    votesGabriel = 0
    votesMarcelo = 0
    votesFernanda = 0
    
    while True:
        chosenOption = input(f"""\nTo vote choose the number corresponding to one of the candidates below:
                1. Gabriel
                2. Marcelo
                3. Fernanda
                4. Check results\n""")
        if chosenOption == "1" or chosenOption == "Gabriel":
            votesGabriel += 1
            print(f"You voted in Gabriel!")
        elif chosenOption == "2" or chosenOption == "Marcelo":
            votesMarcelo += 1
            print(f"You voted in Marcelo!")
        elif chosenOption == "3" or chosenOption == "Fernanda":
            votesFernanda += 1
            print(f"You voted in Fernanda!")
        elif chosenOption == "4" or chosenOption == "Exit":
            print(f"Counting votes...")
            print(f"Gabriel = {votesGabriel} | Marcelo = {votesMarcelo} | Fernanda = {votesFernanda}")
            break
        else:
            print(f"The value {chosenOption} is not valid. Please enter a number corresponding to one of the candidates above.\n")

Main()