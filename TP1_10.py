# TP1.10
# Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random

def Main():
    gender = SelectGender()
    CreateStory(gender)

def SelectGender():
    gender = ["male", "female"]
    numSelected = random.randint(0, 1)
    print(f"\nThe number generated was {numSelected} and the gender is {gender[numSelected]}")
    return gender[numSelected]

def CreateStory(gender):
    emotionMale = ["nervoso", "raivoso", "amoroso", "satisfeito", "feliz"]
    emotionFemale = ["nervosa", "raivosa", "amorosa", "satisfeita", "feliz"]
    local = ["casa", "praça", "loja", "igreja"]
    action = ["riu", "sorriu", "gritou", "esperniou", "chorou"]
    nameMale = ["Gabriel", "Maurício", "João", "Leonardo"]
    nameFemale = ["Alice", "Ana", "Maria", "Luana"]
    
    nameRandom = random.randint(0, 3)
    emotionRandom = random.randint(0, 4)
    localRandom = random.randint(0, 3)
    actionRandom = random.randint(0, 4)
    
    if gender == "male":
        print(f"{nameMale[nameRandom]}, se sentindo {emotionMale[emotionRandom]}, foi a {local[localRandom]} e {action[actionRandom]}...")
    else:
        print(f"{nameFemale[nameRandom]}, se sentindo {emotionFemale[emotionRandom]}, foi a {local[localRandom]} e {action[actionRandom]}...")

Main()