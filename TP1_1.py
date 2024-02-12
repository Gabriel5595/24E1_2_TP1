# TP1.1
## Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

"""
PseudoCode:
1.1. Requisitar primeiro número
1.2. Testar número
1.3. Informar número escolhido

2.1. Requisitar segundo número
2.2. Testar número
2.3. Informar número escolhido

3. Realizar somatório
4. Apresentar resultado
"""

def Main():
    num1 = RequestNumber()
    num2 = RequestNumber()
    SumNumbers(num1, num2)

def RequestNumber():
    while True:
        chosenNumber = input("Type a number: ")
        
        if chosenNumber.isnumeric():
            print(f"The chosen number is {chosenNumber}\n")
            return int(chosenNumber)
        else:
            print(f"Please, type a valid number!\n")

def SumNumbers(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}.")

Main()