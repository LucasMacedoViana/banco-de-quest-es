'''Faça um Programa que peça dois números e imprima o maior deles.


num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numeor: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1<num2:
    print(f'{num2} é maior que  {num1}')
else:
    print('Os números são iguais')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input('Digite um valor: '))
if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
else:
    print('O número é Igual a zero')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido


sexo = input('(F) Feminino \n(M) Masculino \nDigite seu sexo: ')
#utilizei o strip para retirar os possiveis espaços da resposta
if sexo.strip() == 'F' or sexo.strip() == 'f':
    print('Sexo Feminio')
elif sexo.strip() == 'M' or sexo.strip() =='m':
    print('Sexo Masculino')
else:
    print('Sexo invalido')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


vogal = ['a', 'e', 'i', 'o', 'u']
letra = input('Digite uma letra: ')
#utilizei o strip para retirar os possiveis espaços da resposta, o lower para deixcar em minusculo.
if letra.strip().lower() not in vogal:
    print(f'A letra \'{letra.upper()}\' é uma consoate')
else:
    print(f'A letra \'{letra.upper()}\' é uma vogal')'''

#-----------------------------------------------------------------------------------------------------------------------
'''Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Ditie a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Sua média foi {media:.2f} \nAprovado')
elif media == 10:
    print(f'Sua média foi {media:.2f} \nAprovado com Distinção')
else:
    print(f'Sua média foi {media:.2f} \nReprovado')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que leia três números e mostre o maior deles.
lista = []
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'O maior número é o {max(lista, key=float)}')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que leia três números e mostre o maior e o menor deles.
lista = []
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'O maior número é o {max(lista, key=float)}')
print(f'O menor número é o {min(lista, key=float)} ')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.

lista = []
num1 = float(input('Digite o primeiro preço: '))
num2 = float(input('Digite o segundo preço: '))
num3 = float(input('Digite o terceiro preço: '))

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'Você deve comprar o produto que custa R${min(lista, key=float)} ')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(sorted(lista))'''

#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('(M) Manhã \n(T) Tarde \n(N) Noite \nDigite o turno em que você estuda: ')
if turno.lower().strip() == 'm':
    print('Bom Dia')
elif turno.lower().strip() == 't':
    print('Boa tarde')
elif turno.lower().strip() == 'n':
    print('Boa Noite')
else:
    print('Valor Invalido')'''

#-----------------------------------------------------------------------------------------------------------------------
'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.

salario = float(input('Informe seu Salário atual: '))

if salario <= 280:
    percentual = 0.2
elif salario <= 700 and salario > 208:
    percentual = 0.15
elif salario <= 1500 and salario > 700:
    percentual = 0.1
else:
    percentual = 0.05

aumento = salario * percentual
novoSalario = salario + aumento
print(f'Salario antes do Reajuste: R$ {salario} '
      f'\nPercentual de aumento aplicado: {percentual * 100}%'
      f'\nValor do Aumento:R${aumento}'
      f'\nNovo Salário: R${novoSalario}')'''


#-----------------------------------------------------------------------------------------------------------------------

'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

hora = float(input('Digite a quantidade de horas trabalhadas: '))
valorHora = float(input('Digite o valor da hora trabalhada: R$'))
salarioBruto = hora * valorHora

if salarioBruto <= 900:
    ir = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    ir = 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
    ir = 0.1
else:
    ir = 0.2
impostoRenda = salarioBruto * ir
inss = salarioBruto * 0.1
fgts = salarioBruto * 0.11
descontos = impostoRenda  + inss
salarioLiquido = salarioBruto - descontos

print(f'Salario Bruto({hora} * {valorHora})  :R$ {salarioBruto:.2f}')
print(f'(-) IR ({ir * 100}%)                  :R$ {impostoRenda:.2f}')
print(f'(-) INSS (10%)                       :R$ {inss:.2f}')
print(f'FGTS (11%)                           :R$ {fgts:.2f}')
print(f'Total de Descontos                   :R$ {descontos:.2f}')
print(f'Salário Liquido                      :R$ {salarioLiquido:.2f}')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.
dia = int(input('Digite um numero de 1 a 7: '))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sabado')
else:
    print('Valor Invalido')'''

#-----------------------------------------------------------------------------------------------------------------------

'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
#-----------------------------------------------------------------------------------------------------------------------

'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, 
    a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
uma nota de 5 e quatro notas de 1.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''
#-----------------------------------------------------------------------------------------------------------------------
'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''
#-----------------------------------------------------------------------------------------------------------------------
'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''
#-----------------------------------------------------------------------------------------------------------------------
'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''