# TP1.13
# Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

def Main():
    word = input("Type a word: ")
    
    if word == word[::-1]:
        print(f"The given word {word} is the same backwards ({word[::-1]}), so it is a palindrome.")
    else:
        print(f"The given word {word} is not the same backwards ({word[::-1]}), so it is not a palindrome.")

Main()