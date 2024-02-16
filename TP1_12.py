# TP1.12
# Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

def Main():
    word = input(f"Type a word: ")
    
    if len(word) <= 5:
        print(f"This is a {len(word)} letter word, so it is short word")
    else:
        print(f"This is a {len(word)} letter word, so it is long word")

Main()