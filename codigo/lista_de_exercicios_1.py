# Questão 1: Faça um programa que peça dois números inteiros e imprima a soma desses dois números
print('Soma de dois números')

x1 = int(input('Digite o primeiro número para somar:'))
x2 = int(input('Digite o segundo número para somar:'))

print(x1+x2)

#---------------------------------------------------------------------
# Questão 2: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
print('Conversão de metros para milimetros')

metros = int(input('Digite o valor para converter:'))

milimetros = metros*1000

print(milimetros)

#---------------------------------------------------------------------
#Questão 3: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
print('Calculo do total de tempo em segundos')

dias = int(input('Digite o número de dias:'))
horas = int(input('Digite o número de horas:'))
minutos = int(input('Digite o número de minutos:'))
segundos = int(input('Digite o número de segundos:'))

d_to_h = dias*24

h_to_m = (d_to_h*60)+(horas*60)+minutos

min_to_seg = (h_to_m*60) + segundos

print(min_to_seg)

#---------------------------------------------------------------------
#Questão 4: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
print('Calculo do aumento')

salario = int(input('Digite o valor do seu salário:'))
porcentagem = int(input('Digite a porcentagem do seu aumento:'))

aumento = salario * porcentagem/100

total = salario+aumento

print('Salário atual:'+ str(salario))
print('Aumento:' + str(aumento))
print('Salário com aumento:' + str(total))

#---------------------------------------------------------------------
#Questão 5: Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
print('Calculo do desconto do produto')

produto = int(input('Digite o valor do produto:'))
porcentagem = int(input('Digite a porcentagem do desconto:'))

desconto = produto * porcentagem/100

total = produto-desconto

print('Valor do produto:'+ str(produto))
print('Desconto:' + str(desconto))
print('Produto com desconto:' + str(total))

#---------------------------------------------------------------------
#Questão 6: Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
print('Calculo do tempo da sua viajem:')

distancia = int(input('Digite a distância da viajem em Km:'))
velocidade = int(input('Digite a velocidade média que você irá usar durante a viajem em Km/h:'))

tempo = distancia / velocidade


print('Você tera que viajar por:'+ str(tempo) + 'hora(s)')

#---------------------------------------------------------------------
#Questão 7: Converta uma temperatura digitada em Celsius para Fahrenheit.
print('Conversão de Celsius para Fahrenheit:')

C = int(input('Digite a temperatura em Celsius:'))

F = 9*C/5+32

print(str(C) +'° Celsius equivale a ' + str(F) + '° Fahrenheit')


#---------------------------------------------------------------------
#Questão 8: Faça agora o contrário, de Fahrenheit para Celsius.
print('Conversão de Fahrenheit para Celsius:')

F = int(input('Digite a temperatura em Fahrenheit:'))

C = ((F -32) * 5) / 9

print(str(F) +'° Fahrenheit equivale a ' + str(C) + '° Celsius')

#---------------------------------------------------------------------
#Questão 9: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
print('Calculo do preço a pagar:')

distancia = int(input('Digite a quantidade de Km percorrido com o carro:'))
dias = int(input('Digite o número de dias que foi alugado o carro:'))

totalkm = dias * 60
totald = distancia * 0.15
total = totalkm + totald

print('Valor total a se pagar: '+ str(total))

#---------------------------------------------------------------------
#Questão 10: 
# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 1
# 0 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias.
print('Calculo da redução do tempo de vida de um fumante:')

cigarros = int(input('Digite a quantidade de cigarros fumados por dia:'))
anos = int(input('Digite o número de quantos anos que você fuma:'))

total_dias = anos * 365

total = (total_dias * cigarros) / 144

print('Você perdeu: '+ str(total) + ' dias')

#---------------------------------------------------------------------
#Questão 11: Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão
# print('Calculo da quantidades de digitos de  2 elevado a um milhão:')

# print (len(str(2**1000000)))