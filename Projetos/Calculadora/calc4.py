# Calculadora Científica com Módulo math, Inclui funções matemáticas avançadas.

# PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python calc4.py
# Adiciona funcionalidades como raiz quadrada e potência usando o módulo math., Permite que o usuário escolha entre operações básicas e científicas.

import math

def calculator():
    print("Selecione a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Raiz quadrada")
    print("6: Potência")

    choice = input("Digite o número da operação: ")

    try:
        if choice == "5":  # Raiz quadrada
            num = float(input("Digite o número: "))
            print(f"Resultado: {math.sqrt(num)}")
        elif choice == "6":  # Potência
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            print(f"Resultado: {math.pow(base, expoente)}")
        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if choice == "1":
                print(f"Resultado: {num1 + num2}")
            elif choice == "2":
                print(f"Resultado: {num1 - num2}")
            elif choice == "3":
                print(f"Resultado: {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    print(f"Resultado: {num1 / num2}")
            else:
                print("Operação inválida!")
    except ValueError:
        print("Erro: Entrada inválida!")

calculator()


