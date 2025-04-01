#14. Login Bancário
#    • Crie um sistema de login simples: 
#        ◦ Solicite ao usuário o nome de usuário e a senha.
#        ◦ Compare os valores inseridos com credenciais previamente armazenadas em variáveis (ex.: usuario = "admin", senha = "1234").
#        ◦ Exiba mensagens de sucesso ou erro dependendo da entrada.
log = "login"
password = "123"

logconfirn = input("digite seu login :")
passconfirn = input("digite sua senha :")

if logconfirn == log and passconfirn == password:
    print("bem vindo!")
else:
    print("senha ou login invalido, reinicie o progama para tentar novamente!")