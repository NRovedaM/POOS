#Peça ao usuário um número e use if para verificar se ele é positivo, negativo ou zero.
num = int(input("insira um numero: "))

if num > 0:
    print("numero positivo")
elif num == 0:
    print("zero")
else:
    print("numero negativo")