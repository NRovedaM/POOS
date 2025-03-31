#Um banco deseja diminuir a quantidade de contas ativas sem saldo do seu sistema. Desenvolva um algoritmo que verifique o saldo da conta ( solicite essa info ao responsavel pelo acesso) se o saldo for 0 alterar o status da conta para inativo.
cash = float(input("insira o saldo da conta: "))

if cash > 0:
    print("Conta permanece ativa!")
elif cash == 0:
    print("Conta desativada!")
else:
    print("Renegociar a divida")