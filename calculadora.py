# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("criar uma calculadora que some, subtraia, multiplique e divida dois números inteiros")
print("digite o primeiro número: ")
num1 = int(input())
print("digite o segundo número: ")
num2 = int(input())
print("digite a operação desejada: ")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
operacao = int(input())
if operacao == 1:
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
elif operacao == 2:
    resultado = num1 - num2 
    print(f"A subtração de {num1} e {num2} é: {resultado}")
elif operacao == 3:
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é : {resultado}")
elif operacao == 4:
    if num2 != 0:
        resultado = num1 / num2 
        print(f"A divisão de {num1} e {num2} é {resultado}")
else:
        print("Erro: Divsão por 0 não é permitida.")
        print("Operação inválida, por favor, escolha uma operação válida.")
        print("Operação inválida, por favor, escolha outro número.")
        print("Obrigado por usar a calculadora!")
        print("Até a próxima!")
    
