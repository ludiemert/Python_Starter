# Calculadora com Classes, Implementa uma calculadora orientada a objetos.

# Usa uma classe para encapsular as operações matemáticas., Separa a lógica das operações da interação com o usuário.

# executar o codig:  PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python calc5.py

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Erro: Divisão por zero!"
        return x / y

# Instanciar a classe
calc = Calculator()

print("Selecione a operação:")
print("1: Soma")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")

choice = input("Digite o número da operação: ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == "1":
        print(f"Resultado: {calc.add(num1, num2)}")
    elif choice == "2":
        print(f"Resultado: {calc.subtract(num1, num2)}")
    elif choice == "3":
        print(f"Resultado: {calc.multiply(num1, num2)}")
    elif choice == "4":
        print(f"Resultado: {calc.divide(num1, num2)}")
    else:
        print("Operação inválida!")
except ValueError:
    print("Erro: Entrada inválida!")
