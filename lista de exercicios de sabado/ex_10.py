#Crie um programa que peça o valor da compra e use if para calcular o desconto baseado em faixas de preço (exemplo: compras acima de R$100 ganham 10% de desconto).
compra = float(input("insira o valor da compra: "))

if compra >= 100:
    print(f"A compra de {compra}, atingiu o valor minimo para o desconto.\n")
    print(f"valor do desconto é de {compra * 0.10}\n")
    print(f"O valor total a pagar é de {compra - (compra * 0.10):.2f}")
else:
    print("Valor minimo não atingido")