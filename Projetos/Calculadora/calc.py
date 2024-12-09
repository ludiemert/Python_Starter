#executar o prog
#PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python calc.py

import os

print("======")

#Dicionario
operations = {
    "+": "Sum",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "^": "Exponentiation",
}

#programa fica rodando ate pedir para parar
 #enquanto for verdadeiro (enquando o ceu for azul rsrs)
while True: 
    os.system("cls") #limpar a tela
    i = 0
    #operacao escolhida
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operacao que deseja realizar: ")
    op = int(input())
    op_string = list(operations.keys())[op]

    #valor 1 e valor 2
    print("")
    print("{} escolhida.".format(op_string))
    print("")
    try:       
      v1 = float(input("What is the value 1: "))
      v2 = float(input("What is the value 2"))
    except ValueError:
        print("Invalid entry! Make sure you enter numbers.")
        continue

    #definir como fazer as operacoes
    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2
    else:
        print("invalid operation")
        continue

    #apresentar o resultado final com os dados do usuario
    print("")
    print("{} {} {} = {}".format(v1, op_string, v2, result))
    print("")
    print("=======")

    #fim com pergunta se quer continuar ou parar
    print("Do you want to do any more operations? (Type 1 to exit or type any number to return to the menu.)")
    comando = int(input())
    #para o usuario sair
    if comando == 1:
        break




