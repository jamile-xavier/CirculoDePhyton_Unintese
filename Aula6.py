"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120


numero = int(input("Digite o número que deseja calcular o fatorial: "))
resultado = 1

for i in range (numero, 1, -1):
    resultado *= i

print(f"O fatorial do número {numero} é {resultado}")
"""

"""
Altere o programa de cálculo do fatorial , permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e
menores que 16.

- while, if, for, break e continue


while True:
    numero = int(input("Digite um número entre 0 e 16: "))
    if numero < 0 or numero > 16:
        print("Só é aceito números entre 0 e 16")
        continue

    fatorial=1
    for i in range (numero, 1, -1):
        fatorial *= i

    print(f" O resultado de {numero}! é = {fatorial} ")

    if input("Deseja calcular outro fatorial? (s/n): ").lower() != 's':
     print("Até a próxima!")
     break
"""

"""
Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.
"""
print("Verificador de número primo")

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro maior que 1: "))

# Verificação de número menor que 2
if numero <= 1:
    print("Número inválido. Por favor, digite um número maior que 1.")
else:
    divisores = []  # Lista para guardar os divisores

    # Verifica todos os números de 2 até (numero - 1)
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)  # Armazena os divisores

    # Verifica se a lista de divisores está vazia
    if len(divisores) == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} NÃO é primo.")
        print("Ele é divisível por:", end=" ")
        for d in divisores:
            print(d, end=" ")
        print()  # quebra de linha

