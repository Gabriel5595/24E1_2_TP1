# TP1.4
# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.
"""
PseudoCode:
1.1. Crie um loop para continuar perguntando ao usuário uma opção de operação

2.1. Pedir o primeiro número
2.2. verificar se é válido

3.1 Pedir o segundo número
3.2. Verificar se é válido

4.1. Realizar cálculo
4.2. Apresentar resultado
"""

def Main():
    InitOptions()

def InitOptions():
    stillOn = True
    while stillOn == True:
        chosenOption = input(f"""\nChoose the number corresponding to one of the operations below:
                1. Sum
                2. Subtraction
                3. Multiplication
                4. Division
                5. Exit\n""")
        if chosenOption == "1" or chosenOption == "Sum":
            Sum()
        elif chosenOption == "2" or chosenOption == "Subtraction":
            Subtraction()
        elif chosenOption == "3" or chosenOption == "Multiplication":
            Multiplication()
        elif chosenOption == "4" or chosenOption == "Division":
            Division()
        elif chosenOption == "5" or chosenOption == "Exit":
            print(f"Exiting...")
            stillOn = False
        else:
            print(f"The value {chosenOption} is not valid. Please enter a number corresponding to one of the operations above.\n")

def Sum():
    num1, num2 = RequestValue()
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

def Subtraction():
    num1, num2 = RequestValue()
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")

def Multiplication():
    num1, num2 = RequestValue()
    multi = num1 * num2
    print(f"{num1} * {num2} = {multi}")

def Division():
    num1, num2 = RequestValue()
    multi = num1 / num2
    print(f"{num1} / {num2} = {multi}")

def RequestValue():
    num1 = float(input(f"Type the first number: "))
    num2 = float(input(f"Type the second number: "))
    return num1, num2
    
Main()