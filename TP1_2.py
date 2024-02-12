# TP1.2
# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

"""
PseudoCode:
1.1. Recebe minutos do usuário
1.2. Testar número
1.3. Informar número escolhido

2.1. Converter horas em minutos. (Minutos * 60)
2.4 Apresentar resultado (min)

2.1. Recebe horas do usuário
2.2. Testar número
1.3. Informar número escolhido

2.1. Converter horas em minutos. (Horas / 60)
2.2. Realizar conta para saber o resto. (Horas % 60)
2.2 Apresentar resultado (h e min)
"""

def Main():
    chosenHours = RequestHours()
    HoursToMinutes(chosenHours)
    chosenMinutes = RequestMinutes()
    MinutesToHours(chosenMinutes)
    

def RequestHours():
    while True:
        chosenHours = input("Type a number of hours to transform into minutes: ")
        
        if chosenHours.isalpha():
            print(f"Please, type a valid number ou hours!\n")
        elif float(chosenHours) < 0:
            print(f"Please, type a valid number ou hours!\n")
        else:
            print(f"The chosen number is {chosenHours}\n")
            return float(chosenHours)
        
def RequestMinutes():
    while True:
        chosenMinutes = input("Type a number of minutes to transform into hours: ")
        
        if chosenMinutes.isalpha():
            print(f"Please, type a valid number ou minutes!\n")
        elif float(chosenMinutes) < 0:
            print(f"Please, type a valid number ou minutes!\n")
        else:
            print(f"The chosen number is {chosenMinutes}\n")
            return float(chosenMinutes)
    
def HoursToMinutes(numberOfHours):
    minutes = numberOfHours * 60
    print(f"{numberOfHours}h = {minutes:.0f}min")

def MinutesToHours(chosenMinutes):
    hours = (chosenMinutes // 60)
    minutes = (chosenMinutes % 60)
    print(f"{chosenMinutes}min = {hours:.0f}h and {minutes:.0f}min")
    

Main()