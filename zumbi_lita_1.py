__author__ = 'rosenclevergazoni'

#exercicio_1
"""
num1 = int (input("Informe o primeiro número:"))
num2 = 10int (input("Informe o segundo número:"))
print("Soma: %d" %(num1+num2))
"""
#exercício_2
"""
valor = int (input("Informe o valor em metros: "))
print("O valor %d convertido de metros para milímetros é  %.2f" %(valor, float(valor*1000.1)))
"""

#exercício_3
"""
dias = int(input("Informe o total de dias: "))
horas = int(input("Informe o total de horas: "))
minutos = int(input("Informe o total de minutos: "))
segundos = int(input("Informe o total de segundos: "))

print("total de segundos correspondente aos dias %d informados: %d" %(dias, dias*24*60*60))
print("total de segundos correspondente as horas %d informadas: %d" %(horas, horas*60*60))
print("total de segundos correspondente aos minutos %d informados: %d" %(minutos, minutos*60))
print("total de segundos segundos informados: %d" %(segundos))
print("total de segundos correspondente so tempo total informado: %d" %(dias*24*60*60 + horas*60*60 + minutos*60 + segundos))
"""

#exercício_4
"""
salario = float(input("Informe o salário: "))
aumento = float(input("informe o percentual de aumento: "))
print("Para o salário %.2f foi concedido um aumento de %.2f " %(salario, aumento))
print("O novo salário: %.2f" %(salario + (salario * aumento / 100)))
"""

#exercício_5
"""
mercadoria = float(input("Informe o valor mercadoria: "))
desconto = float(input("informe o percentual de desconto: "))
print("Para a mercadoria com valor %.2f foi concedido um desconto de %.2f " %(mercadoria, desconto))
print("O novo salário: %.2f" %(mercadoria - (mercadoria * desconto / 100)))
"""

#exercício_6
"""
distancia = float(input("Informe a distância: "))
velocidadeMedia = float(input("informe a velocidade Média: "))
print("Para a distância %.2f KM percorrida a uma velocidade média de %.2f KM/h o tempo previsto para a viagem é %.2fh"
      %(distancia, velocidadeMedia, (distancia/velocidadeMedia)))
"""
#exercício_7
"""
celsius = float(input("Informe a temperatura (C): "))
fahrenheit =  9 * celsius / 5 + 32
print("Para a temperatura %.2f C a sua correspondente em Fahrenheit é %.2f F" %(celsius, fahrenheit))
"""

#exercício_8
"""
fahrenheit = float(input("Informe a temperatura (F): "))
celsius =  (fahrenheit - 32) / (9 / 5)
print("Para a temperatura %.2f F a sua correspondente em Celsius é %.2f C" %(fahrenheit, celsius))
"""

#exercício_9
"""
distancia = float(input("Informe a distância percorrida: "))
dias = int(input("informe total de dias do aluguel: "))
print("Para distância percorrida de %.2f nos %d dias alugados, o valor da locação é R$%.2f"
      %(distancia, dias, (60*dias + 0.15*distancia) ))
"""

#exercício_10
"""
totalCigarrosDia = float(input("Informe o total de cigarros que se fuma por dia: "))
totalAnos = int(input("Informe o total de anos fumando: "))
minutosPerdidos = totalCigarrosDia * 10 * 365 * totalAnos
diasPerdidos = (minutosPerdidos / (60*24)) # minutos * horas * ano
print("De acordo com os valores informados você vai viver %d dias a menos" %diasPerdidos)
"""

#exercício_11
"""
resultado = 2 ** 1000000
totalDigitos = len((str(resultado)))
print("%d" %totalDigitos)
"""

#exemplo Vetor orden crescente
vet = [4, 2, 10, 1]
for i in range(len(vet)):
    j = i + 1
    for j in range(len(vet)):
        if (vet[i] < vet[j]):
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux
print(vet)
