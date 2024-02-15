# TP1.4
# Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

def Main():
    age = int(RequestsAge())
    ChecksAge(age)

def RequestsAge():
    while True:
        age = input("\nType your age: ")
        if age.isdecimal():
            return age
        else:
            print(f"The respose {age} is not a number. Please provide your age.")

def ChecksAge(age):
    if age >= 18:
        print("You are of legal age.")
    else:
        print("You are underage.")

Main()