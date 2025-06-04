"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.

import math

metros_quadrados = float(input("Quantos metros quadrados?"))

latas = math.ceil(metros_quadrados/ 54)

preco = latas * 80

print(f"Você precisa comprar {latas:.0f}, custando R${preco:.2f}")

"""

"""
Faça um programa que pela dois números e imprima o maior deles

num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))

if num1 > num2:
    print(num1)
if num2 > num1:
    print(num2)    
if num1 == num2:
    print("Os números são iguais")

if (num1 > num2) or (num1 < num2):
    print("Os números são diferentes")

if num1 > num2 and num1 > 0:
    print("O primeiro valor é maior e positivo")
    """
"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ["a", "e", "i", "o", "u"]

letra_digitada = input("Digite uma letra: ").lower()

if letra_digitada.isalpha() and len(letra_digitada) == 1:
    if letra_digitada in vogais:
        print(f"A letra {letra_digitada} é uma vogal")
    else:
        print(f"A letra {letra_digitada} é uma consoante")
else:
    print("Por favor, digite apenas uma letra!")
"""

"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :
        aumento de 5% Após o aumento ser realizado,
    informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

