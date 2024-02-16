# TP1.11
# Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random

def Main():
    diceAmount = int(input("How many dices you would like to roll? "))
    
    results = []
    rolls = 0
    while rolls != diceAmount:
        roll = random.randint(1, 6)
        results.append(roll)
        rolls += 1
    
    print(f"The results of {diceAmount} rolls was {results}")

Main()