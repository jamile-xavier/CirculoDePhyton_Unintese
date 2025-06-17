"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.


print("Leitura de média do aluno")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if  9 >= media <=10:
    print(f"As notas digitadas são: {nota1} e {nota2}, a média dessas notas é {media}, o conceito é A, situação do aluno: Aprovado.")
elif 7.5 >= media < 9:
    print(f"As notas digitadas são: {nota1} e {nota2}, a média dessas notas é {media}, o conceito é B, situação do aluno: Aprovado.")
elif 6 >= media < 7.5:
    print(f"As notas digitadas são: {nota1} e {nota2}, a média dessas notas é {media}, o conceito é C, situação do aluno: Aprovado.")
elif 4 >= media < 6:
    print(f"As notas digitadas são: {nota1} e {nota2}, a média dessas notas é {media}, o conceito é D, situação do aluno: Reprovado.")
elif 0 >= media < 4:
    print(f"As notas digitadas são: {nota1} e {nota2}, a média dessas notas é {media}, o conceito é E, situação do aluno: Reprovado.")
else:
    print("Os dados informados são inválidos!")
"""
"""
Faça um programa que peça uma nota, entre zero a dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informa um valor válido.

nota = float(input("Digite sua nota: "))
while nota < 0 or nota > 10:
    nota = float(input("Número inválido. Digite sua nota novamente: "))
"""

"""
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""
# Validação do nome
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Nome deve ter mais de 3 caracteres!")
    nome = input("Digite seu nome novamente: ")

# Validação da idade
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade deve estar entre 0 e 150 anos!")
    idade = int(input("Digite sua idade novamente: "))

# Validação do salário
salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Salário deve ser maior que zero!")
    salario = float(input("Digite seu salário novamente: "))

# Validação do sexo
sexo = input("Digite seu sexo (f/m): ").lower()
while sexo not in 'fm':
    print("Sexo deve ser 'f' ou 'm'!")
    sexo = input("Digite seu sexo novamente (f/m): ").lower()

# Validação do estado civil
estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
while estado_civil not in 'scvd':
    print("Estado civil deve ser 's', 'c', 'v' ou 'd'!")
    estado_civil = input("Digite seu estado civil novamente (s/c/v/d): ").lower()

# Exibição dos dados validados
print("\nDados validados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo.upper()}")
print(f"Estado Civil: {estado_civil.upper()}")

