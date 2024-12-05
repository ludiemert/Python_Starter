# Calculadora Simples com Funções
# executart o prog => PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python .\calc1.py OU python calc1.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

# Menu de opções
print("Selecione a operação:")
print("1: Adição")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")

# Entrada do usuário
choice = input("Digite o número da operação (1/2/3/4): ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == "1":
        print(f"Resultado: {add(num1, num2)}")
    elif choice == "2":
        print(f"Resultado: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Resultado: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Operação inválida!")
except ValueError:
    print("Erro: Entrada inválida!")
