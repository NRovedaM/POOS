#15. Simulação de Compra no Mercado
#    • Desenvolva um programa que: 
#        ◦ Solicite ao usuário o nome de um produto, a quantidade comprada e o preço unitário.
#        ◦ Calcule e exiba o total da compra (ex.: Total: R$ [valor calculado]).
#        ◦ Aplique um desconto de 5% se o valor total for maior que R$100.
product = input("insira o nome do produto: ")
amount = int(input("insira a quantidade de itens comprados: "))
price_unit = float(input("insira o valor unitario do item: "))

product_total = price_unit * amount
print(f"valor da compra é de R${product_total:.2f}")

if product_total >= 100:
    print(f"desconto concedido por ultrapassar valor minimo de R$ 100.00 total a pagar é R${product_total - (product_total * 0.05):.2f}")
else:
    print(f"total a pagar R${product_total:.2f}")
print(f"aproveite seus(suas) {product}s")