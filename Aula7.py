"""
Fácil
Ferramentas DISPONÍVEIS: for, if, print.

Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.

print("Programa para apuração de votos")

# Iniciar o contador de votos
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_nulos = 0

# Obter o número de eleitores
numero_eleitores = int(input("Qual o número total de eleitores? "))

# Obter votos de cada candidato
for i in range(1, numero_eleitores + 1):
    print(f"\nEleitor {i}:")
    voto_candidato = int(input("Digite o número do candidato que você deseja votar (1, 2 ou 3): "))

    if voto_candidato == 1:
        votos_candidato_1 += 1
        print("Você votou no candidato 1!")
    elif voto_candidato == 2:
        votos_candidato_2 += 1
        print("Você votou no candidato 2!")
    elif voto_candidato == 3:
        votos_candidato_3 += 1
        print("Você votou no candidato 3!")
    else:
        print("O número digitado é inválido, seu voto foi anulado.")
        votos_nulos += 1

# Exibir o resultado da apuração
print("\nRESULTADO DA APURAÇÃO:")
print(f"O número de votos do candidato 1 é: {votos_candidato_1}")
print(f"O número de votos do candidato 2 é: {votos_candidato_2}")
print(f"O número de votos do candidato 3 é: {votos_candidato_3}")
print(f"O número de votos nulos é: {votos_nulos}")
"""
"""
VALE TUDO

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
alto, o mais baixo, a mais pesado e o mais leve, para isto você deve fazer um
programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
no campo código.

Ao encerrar o programa também deve ser informados os códigos e valores do
cliente mais alto, do mais baixo, do mais pesado e do mais leve, além da média
das alturas e dos pesos dos clientes.
"""