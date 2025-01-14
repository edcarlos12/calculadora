# Calculadora em Python 

def soma(numero_1, numero_2):
    return numero_1 + numero_2

def subtracao(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacao(numero_1, numero_2):
    return numero_1 * numero_2

def divisao(numero_1, numero_2):
    if numero_1 == 0 or numero_2 == 0:
        return "Erro! Divisão por zero não é permitido."
    else:
        return numero_1 / numero_2

def calculadora():
    print("Operações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    operacao = input("Escolha a operação (1/2/3/4): ")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif operacao == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif operacao == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif operacao == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Operação inválida! Por favor, escolha uma opção de 1 a 4.")
    except ValueError:
        print("Erro! Por favor, insira um número válido.")

# Chama a função da calculadora
calculadora()
