# TP1.7
# Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

def main():
    peso = float(recebePeso())
    altura = float(recebeAltura())
    Imc = calculaIMC(peso, altura)
    verificaIMC(Imc)

def recebePeso():
    peso = int(input("Digite o seu peso: "))
    return peso

def recebeAltura():
    altura = float(input("Digite o seu altura em metros: "))
    return altura

def calculaIMC(peso, altura):
    Imc = peso / (altura * altura)
    print(f"O seu IMC é de {Imc:.1f}")
    return Imc

def verificaIMC(Imc):
    if (Imc < 18.5):
        print("Você está abaixo do peso para a sua altura.")
    elif (Imc >= 18.5) and (Imc <= 24.9):
        print("Você esta com peso adequado para a sua altura.")
    elif (Imc >= 25) and (Imc <= 29.9):
        print("Você está com sobrepeso para a sua altura.")
    elif (Imc >= 30) and (Imc <= 34.9):
        print("Você tem Obesidade Grau I para a sua altura.")
    elif (Imc >= 35) and (Imc <= 39.9):
        print("Você tem Obesidade Grau II para a sua altura.")
    elif (Imc >= 40):
        print("Você tem Obesidade Grau III para a sua altura.")

main()