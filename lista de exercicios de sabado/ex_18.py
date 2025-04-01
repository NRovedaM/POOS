#18. Cálculo de Salário com Horas Extras
#    • Crie um programa que: 
#        ◦ Peça o salário base, o número de horas extras trabalhadas e o valor pago por hora extra.
#        ◦ Calcule o salário total (base + horas extras).
#        ◦ Exiba o valor total do salário.
wage = float(input("insira seu salario"))
hours = int(input("insira a quantidade de horas extras"))
hours_paid = float(input("insira o valor pago na sua hora extra"))

pay = hours_paid * hours

print(f"seu salario final é de R${pay + wage:.2f}")