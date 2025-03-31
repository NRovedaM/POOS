#Crie um programa que peça ao usuário um nome de usuário e senha e use if para verificar se as credenciais estão corretas.
#escolhi um valor fixo para login e senha para facilitar
log = "login"
password = "123"

logconfirn = input("digite seu login :")
passconfirn = input("digite sua senha :")

if logconfirn == log and passconfirn == password:
    print("bem vindo!")
else:
    print("senha ou login invalido, reinicie o progama para tentar novamente!")