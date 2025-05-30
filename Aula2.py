import math
#print("Cálculo da área de um círculo")
#raio = float(input("Digite o raio do círculo: "))
#area = 3.14159 * (raio**2)
#print(f"O valor da área é de {area:.2f}")

#Dar preferência ao usar os dados como variável, no exemplo acima colocar um pi em uma variável.

#print(f"O valor do pi é = {math.pow(2,3)}")

#print("Cálculo salarial")
#valorHora = float(input("Quanto você recebe por hora trabalhada? "))
#numeroHoras= float(input("Quantas horas você trabalhou esse mês? "))
#horasExtras50= float(input("Você realizou horas extras 50%? Se sim, quantas horas? Se não digite 0: "))
#horasExtras100= float(input("Você realizou horas extras 100%? Se sim, quantas horas? Se não digite 0: "))
#totalSalario= (valorHora*numeroHoras) + ((valorHora+(valorHora/2))*horasExtras50) + ((valorHora*2)*horasExtras100)
#print(f"O valor do seu salário esse mês é de R${totalSalario:.2f}")


print("Cálculo de holerite")
valorHora = float(input("Quanto você recebe por hora trabalhada? "))
numeroHoras= float(input("Quantas horas você trabalhou esse mês? "))
horasExtras50= float(input("Você realizou horas extras 50%? Se sim, quantas horas? Se não digite 0: "))
horasExtras100= float(input("Você realizou horas extras 100%? Se sim, quantas horas? Se não digite 0: "))
salarioBruto = math.fsum([
    math.prod([valorHora, numeroHoras]),
    math.prod([valorHora * 1.5, horasExtras50]),
    math.prod([valorHora * 2, horasExtras100])
])
porcentagemIR = 0.11
porcentagemInss = 0.08
porcentagemSindicato = 0.05
descontoIr = math.prod([salarioBruto, porcentagemIR])
descontoInss= math.prod([salarioBruto, porcentagemInss])
descontoSindicato = math.prod([salarioBruto, porcentagemSindicato])
totalDescontos = math.fsum([descontoIr, descontoInss, descontoSindicato])
salarioLiquido = salarioBruto - totalDescontos
print(f"O valor do seu salário bruto esse mês é de R${salarioBruto:.2f}")
print(f"Você pagou R${descontoIr:.2f} de imposto de renda")
print(f"Você pagou R${descontoInss:.2f} de INSS")
print(f"Você pagou R${descontoSindicato:.2f} de contribuição sindical")
print(f"O total de descontos foi de R${totalDescontos:.2f}")
print(f"Esse mês você receberá um salário de R${salarioLiquido:.2f}")