#Escreva um programa que receba dois números e uma operação (adição, subtração, multiplicação ou divisão). Use if para realizar a operação correta com base na escolha do usuário.
num = int(input("insira o primeiro numero: "))
numm = int(input("insira o segundo numero: "))
vari = input("insira qual  operação deseja fazer dentro das seguintes:"
"\n (+)soma, (-)subitrair, (*)multiplicar, (/)dividir: ")
print("o resultado é: ")

if vari == "+":
    print(num + numm)
elif vari == "-":
    print(num - numm)
elif vari == "*":
    print(num * numm)
elif vari == "/":
    print(num / numm)
else:
    print("comando invalido reinicie o programa e recomece a operação")