#13. Cadastro de Alunos em uma Escola
#   • Escreva um programa que: 
#        ◦ Solicite o nome, idade e turma de um aluno.
#        ◦ Armazene as informações em variáveis.
#        ◦ Exiba uma mensagem como: “Aluno cadastrado com sucesso: [Nome], [Idade] anos, turma [Turma].”
#        ◦ Verifique se a idade é maior ou igual a 6 anos para validar a matrícula.
name = input("insira seu nome: ")
age = int(input("insira sua idade: "))
clas = input("insira qual classe você pertence: ")

if age >= 6:
    print(f"Aluno cadastrado com sucesso: {name}, {age} anos, turma {clas}.")
else:
    print("muito novo")