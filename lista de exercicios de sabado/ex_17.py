#17. Verificação de Maiores de Idade
#    • Desenvolva um programa que: 
#        ◦ Solicite a idade de uma pessoa.
#        ◦ Exiba uma mensagem informando se ela é maior de idade (≥ 18 anos) ou não.
age = int(input("insira sua idade"))

if age >= 18:
    print("maior de idade")
else:
    print("menor de idade")