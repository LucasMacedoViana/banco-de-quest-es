while True:
    operacao = input('''    (+) soma
    (-) Subtração
    (*) Multiplicação
    (/) Divisão
    (**) Expotenciação
    (//)Divisão interia
    Digite uma operação: ''')
    if operacao == "":
        print("Digite uma operação valida")
        break

    num01 = float(input("Digite o primeiro número: "))
    num02 = float(input("Digite o segundo número: "))

    def somar(num01, num02):
        print(f'{num01} + {num02} = {num01 + num02:.2f}')
    def subtrair(num01, num02):
        print(f'{num01} - {num02} = {num01 - num02:.2f}')
    def multiplicar(num01, num02):
        print(f'{num01} x {num02} = {num01 * num02:.2f}')
    def dividir(num01, num02):
        print(f'{num01} / {num02} = {num01 / num02:.2f}')
    def expotenciacao (num01, num02):
        print(f'{num01} ** {num02} = {num01 ** num02:.2f}')
    def inteira(num01, num02):
        print(f'{num01} // {num02} = {num01 // num02:.2f}')


    while True:
        if operacao == '+':
            somar(num01,num02)
            break
        elif operacao == '-':
            subtrair(num01, num02)
            break
        elif operacao == '*':
            multiplicar(num01, num02)
            break
        elif operacao == '/':
            dividir(num01, num02)
            break
        elif operacao == '**':
            expotenciacao(num01, num02)
            break
        elif operacao == '//':
            inteira(num01, num02)
            break

    parar = input("(s) sim \n(n) não \nDeseja fazer outra operação? ")
    if parar != 's':
        print('Encerrando a calculadora!')
        break
    else:
        continue