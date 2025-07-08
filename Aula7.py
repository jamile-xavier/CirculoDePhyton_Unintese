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

print("Senso da Academia")

# Variáveis para armazenar os dados iniciais
mais_alto = 0
cod_mais_alto = 0

mais_baixo = 999
cod_mais_baixo = 0

mais_pesado = 0
cod_mais_pesado = 0

mais_leve = 999
cod_mais_leve = 0

# Variáveis para calcular médias
soma_alturas = 0
soma_pesos = 0
quantidade_clientes = 0

while True:
    codigo = int(input("Digite o código do cliente (0 para sair): "))
    
    if codigo == 0:
        break

    altura = float(input("Digite a altura do cliente (em metros, exemplo: 1.75): "))
    peso = float(input("Digite o peso do cliente (em kg): "))
    
    # Atualiza totais
    soma_alturas += altura
    soma_pesos += peso
    quantidade_clientes += 1

    # Verifica o mais alto
    if altura > mais_alto:
        mais_alto = altura
        cod_mais_alto = codigo

    # Verifica o mais baixo
    if altura < mais_baixo:
        mais_baixo = altura
        cod_mais_baixo = codigo

    # Verifica o mais pesado
    if peso > mais_pesado:
        mais_pesado = peso
        cod_mais_pesado = codigo

    # Verifica o mais leve
    if peso < mais_leve:
        mais_leve = peso
        cod_mais_leve = codigo

# Mostra os resultados
print("\n--- RESULTADOS DO SENSO ---")

if quantidade_clientes > 0:
    print(f"Cliente mais alto: Código {cod_mais_alto} - Altura: {mais_alto:.2f} m")
    print(f"Cliente mais baixo: Código {cod_mais_baixo} - Altura: {mais_baixo:.2f} m")
    print(f"Cliente mais pesado: Código {cod_mais_pesado} - Peso: {mais_pesado:.2f} kg")
    print(f"Cliente mais leve: Código {cod_mais_leve} - Peso: {mais_leve:.2f} kg")

    media_altura = soma_alturas / quantidade_clientes
    media_peso = soma_pesos / quantidade_clientes

    print(f"Média das alturas: {media_altura:.2f} m")
    print(f"Média dos pesos: {media_peso:.2f} kg")
else:
    print("Nenhum cliente foi cadastrado.")