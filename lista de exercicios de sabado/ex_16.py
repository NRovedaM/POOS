#16. Cálculo de Média de Notas
#    • Faça um programa que: 
#        ◦ Peça ao usuário três notas.
#        ◦ Calcule a média aritmética das notas.
#        ◦ Informe se o aluno está aprovado (média ≥ 7), em recuperação (média entre 5 e 7) ou reprovado (média < 5).
nota1 = int(input("insira a primeira nota: "))
nota2 = int(input("insira a segunda nota: "))
nota3 = int(input("insira a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"a media do aluno é {media:.1f}")

if media > 7:
    print("aprovado")
elif media > 5:
    print("recuperação")
else:
    print("reprovado")