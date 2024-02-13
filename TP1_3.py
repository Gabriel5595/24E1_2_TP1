# TP1.3
# Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome

"""
PseudoCode:
1.1. Pede o primeiro nome ao usuário
1.2. Verifica se o nome pedido tem mais de três letras
1.3. Pede o Segundo nome ao usuário
1.4. Verifica se o nome pedido tem mais de três letras

2.1. Pega as primeiras 3 letras do primeiro nome
2.2. Pega as últimas três letras do segundo nome
2.3. Junta as duas seleções
2.4. Apresenta na tela
"""

def Main():
    firstName, secondName = RequestNames()
    GeneratesNewName(firstName, secondName)

def RequestNames():
    while True:
        firstName = input("Input the first name: ")
        if len(firstName) < 3:
            print(f"The name {firstName} has less then 3 letters. Please enter a name with at least 3 letters.\n")
        else:
            print(f"The first inserted name was {firstName}\n")
            break
    
    while True:
        secondName = input("Input the second name: ")
        if len(secondName) < 3:
            print(f"The name {secondName} has less then 3 letters. Please enter a name with at least 3 letters.\n")
        else:
            print(f"The second inserted name was {secondName}\n")
            break
    
    return firstName, secondName

def GeneratesNewName(firstName, secondName):
    part1 = firstName[:3]
    part2 = secondName[-3:]
    newName = part1 + part2
    print(f"The new name is {newName}")

Main()