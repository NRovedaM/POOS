#Faça um algoritmo que realize o cadastro de uma pessoa, a senha deve ter no minimo 8 caracteres. O email cadastrado deve estar todo minusculo, depois solicite o login com os dados cadastrados.
#email
log_new = input("\ndigite seu email para cadastro: ")
log_new = log_new.lower()

#senha
pass_new = input("\ndigite a senha com 8 digitos: ")
size_pass = len(pass_new)

#vereficação de senha
if size_pass > 8:
    print("\nsenha invalida, mais que 8 digitos, reinicio o processo")
else:
    print("\ncadastro concluido com sucesso!")

    #login e verificação de login
    print("\nfaça seu login com as informações do cadastro")
    log = input("\ninsira email/usuario: ")
    password = input("insira a senha: ")

    if log_new == log and pass_new == password:
        print("\nBem vindo")
    else:
        print("\nLogin ou Senha incorreto, refaça todo processo")