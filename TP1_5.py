# TP1.5
# Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, combine-os para formar uma saudação personalizada.

def Main():
    firstName = input("Type the first name: ")
    lastName = input("Type the last name: ")
    
    print(f"Olá, {firstName} {lastName}!")

Main()