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
