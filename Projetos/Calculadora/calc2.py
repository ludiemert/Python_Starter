# Calculadora com eval() => Usa a função eval() para calcular diretamente as operaçõe
# Permite que o usuário insira uma expressão matemática completa (por exemplo, 2 + 3 * 4).

# executar o codig => PS C:\Users\user\Downloads\Computer_Vision_Py\Calculadora> python .\calc2.py


# Trata erros como entradas inválidas e suporta múltiplas operações.
while True:
    try:
        print("Digite uma operação matemática ou 'sair' para encerrar:")
        expression = input("> ")
        if expression.lower() == "sair":
            print("Encerrando a calculadora...")
            break
        result = eval(expression) # funcao eval, Usa eval() para avaliar a expressão e calcular o resultado.
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"Erro: {e}")


