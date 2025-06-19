'''#variaveis

largura = 40

#listas

sexoList = {
    "f": "feminino",
    "m": "masculino"
}

estadoCivilList {
    "s": "Solteiro",
    "c": "Casado",
    "v": "Viúvo"
}

#teste[0]
#teste[1]
teste = 'abc'
len(teste)
'''
"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro
Depois modifique o programa para que ele mostre os números um ao lado do outro


for i in range(1,21):
    print(i)

numeros = ""
for i in range(1,20):
    numeros += f"{i}, "
numeros += "20"
print(numeros)


letras = 'abc'
print(letras.index('a'))

letras = ['a', 'b', 'c']
print(letras.index('a'))


print("STRINGS")
letras = 'abc'
for palavra in letras:
    primeiraLetra = palavra
    break
print(primeiraLetra)

print("----------------")

print("VETOR")
letras = ['a', 'b', 'c']
for palavra in letras:
    print(palavra)
"""

# DESAFIOS DA SEMANA:
"""
Fácil:

Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.

numero_base = int(input("Digite o número base: "))
numero_expoente = int(input("Digite o número expoente: "))
resultado = 1

for i in range(numero_expoente):
        resultado *= numero_base
        
print(f"O Resultado é: {resultado}")

"""


"""
Difícil:
DICA: math, while, if, for.

Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
Apenas números entre 0 e 1000

DICA EXTRA:
Existe uma constante para infinito.
"""
import math

# Entrada do número total de valores
quantidade_de_numeros = int(input("Quantos números você deseja digitar? "))

# Inicialização das variáveis
menor = math.inf       # Começa com infinito positivo
maior = -math.inf      # Começa com infinito negativo
soma = 0               # Soma dos números
contador = 1           # Contador para controlar o loop

while contador <= quantidade_de_numeros:
    # Entrada do número atual
    numero = float(input(f"Digite o {contador}º número: "))
    
    # Validação do intervalo
    if numero < 0 or numero > 1000:
        print("Número inválido! Digite um número entre 0 e 1000.")
        continue
    
    # Atualização dos valores
    menor = min(menor, numero)
    maior = max(maior, numero)
    soma += numero
    
    contador += 1

# Exibição dos resultados
print("\nRESULTADOS:")
print(f"Menor valor: {menor:.2f}")
print(f"Maior valor: {maior:.2f}")
print(f"Soma dos valores: {soma:.2f}")