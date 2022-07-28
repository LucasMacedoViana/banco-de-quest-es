'''Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print('Alo Mundo')'''

'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num = float(input('Informe um número: '))
print(f'O número informado foi {num}')'''

'''Faça um Programa que peça dois números e imprima a soma.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número:  '))
soma = num1 + num2
print(f' {num1} + {num2} = {soma}')'''

'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Informa a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nora: '))
nota4 = float(input('Informa a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/ 4
print(f'A média é {media:.2f}')'''

'''Faça um Programa que converta metros para centímetros.

metros = int(input('Informe a distância em metros: '))
converter = metros * 100
print(f'{metros}m equivale a {converter}cm')'''

'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raio = float(input('Informe o raio do circulo: '))
area = math.pi*(raio**2)
print(f'A area do ciculo é {area:.2f}')'''

'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = float(input('Informe o tamanho de um dos lados do quadrado: '))
area = quadrado ** 2
print(f'A area do quadrado é: {area} o seu dobro é: {area*2}')'''

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Informe o valor da hora do funcionario: '))
horaTrabalhada = float(input('Informe quantas horas o funcionario trabalhou: '))
salario = valorHora * horaTrabalhada
print(f'O funcionario deve receber R${salario:.2f}')'''

'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))
celcius = 5*((fahrenheit -32) /9)
print(f'A temperatura em Celcius é {celcius:.2f}ªC')'''

'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius = float(input('Informe a temperatura em Celcius: '))
fahrenheit = 32 + (celcius * (9/5))
print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}ªF')'''

'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
num3 = float(input("Infome o terceiro número: "))

a = (2 * num1) * (num2/2)
b = (num1 * 3) + num3
c = num3 ** 3
print(f'({num1} * 2) * ({num2} / 2) = {a}')
print(f'({num1} * 3) + {num3} = {b}')
print(f'{num3} * {num3} * {num3} = {c}')'''

'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Infome sua altura: '))
peso = (72.7 * altura) - 58
print(f'Seu peso ideal é: {peso:.2f}Kg')'''

'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

while True:
    sexo = input('(H) Homem \n(M) Mulher \nInforme seu sexo:  ')
    if sexo == 'h' or sexo == "H":
        altura = float(input('Informe sua altura: '))
        homem = (72.7 * altura) - 58
        print(f'Seu peso ideal é {homem:.2f}Kg')
        break
    elif sexo == "m" or sexo == "M":
        altura = float(input('Informe sua altura: '))
        mulher = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é {mulher}')
        break
    else:
        print('Informe o sexo corretamente')'''

'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Peso do pescado: '))
if peso > 50:
    multa = (50 - peso) * 4
    if multa < 0:
        print(f'O apurado excedeu o limite em {(50 - peso)*-1} Kg, você deve pagar uma multa de R${multa * -1:.2f}')
    else:
        print(f'O apurado excedeu o limite em {50 - peso} Kg, você deve pagar uma multa de R${multa:.2f}')
else:
    print('Apurado dentro do limite permitido!')'''

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido


valorHora = float(input('Informe o valor da hora trabalhada R$ '))
horasTrabalhada = float(input('Informe a qantidade de horas trabalhadas: '))
salarioBruto = horasTrabalhada * valorHora
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato
print(f'+ Salário Bruto: {salarioBruto:.2f}')
print(f'- IR (11%): R$ {impostoRenda:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicato (5%): R$ {sindicato}')
print(f'= Salário Liquiedo: R$ {salarioLiquido:.2f}')'''

'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


import math

areaPintada = float(input("Digite a metragem da área pintada: "))
calcularLitros = areaPintada / 3
#54 equivale a quantos metros quadrados uma lata pinta
calcularLatas = areaPintada / 54
valorDaCompra = float(math.ceil(calcularLatas)* 80)

print(f'Quantidade de Lata(s): {math.ceil(calcularLatas)} \nValor da compra:R$ {valorDaCompra:.2f} ')'''

'''Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
#input da area pintada
areaPintada = float(input("Digite a metragem da área pintada: "))
#Calculando latas 18 litros
#108 equivale a quantos metros quadrados uma lata de 18 litros pinta, tendo em vista que 1 litro pinta 6 metros quadrados
calcularLatas = areaPintada / 108
comprarLatas = float(math.ceil(calcularLatas)* 80)
#Calculando galões 3.6l
#21.6 equivale a quantos metros quadrados um galão de 3.6 litros pinta.
calcularGaloes = areaPintada / 21.6
comprarGaloes = float(math.ceil(calcularGaloes)* 25)
#Misturando
sobraLatas = areaPintada % 108
sobraGaloes = (sobraLatas / 21.6) * 1.1
comprarMisturado = (math.floor(calcularLatas)*80) + (math.ceil(sobraGaloes) * 25)

print(f'1 - {math.ceil(calcularLatas)} Latas        valor: R${comprarLatas:.2f}')
print(f'2 - {math.ceil(calcularGaloes)} Galões       valor: R${comprarGaloes:.2f}')
print(f'3 - Misturando {math.floor(calcularLatas)}Latas     {math.ceil(sobraGaloes)} Galões     valor: R${comprarMisturado:.2f}')'''




'''Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('EM MB \nInforme o tamanho do arquivo: '))
velocidade = float(input('ME Mb/s \nInforme a velocidade da internet: '))
tempo = (arquivo/(velocidade / 8)) / 60
print(f'Tempos estimado de Download {tempo:.1f} Minutos')'''




























