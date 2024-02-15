# TP1.4
# Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc.

def Main():
    value = RequestValue()
    discount = GeneratesDiscount(value)
    AppliesDiscount(value, discount)

def RequestValue():
    while True:
        value = input("\nType the value of the product: ")
        if value.isalpha():
            print(f"Please, type a valid number ou hours!\n")
        elif float(value) < 0:
            print(f"Please, type a valid number ou hours!\n")
        else:
            return float(value)

def GeneratesDiscount(value):
    if value < 100:
        return 0
    elif value >= 100 and value < 150:
        return 0.1
    else:
        return 0.15

def AppliesDiscount(value, discount):
    newValue = value * (1 - discount)
    print(f"In a ${value} purchase, there is a discount of {discount * 100}%. The new value is ${newValue}.")

Main()