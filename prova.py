import math
ano = int(input("Digite o Ano:"))

def descobrirSeculo():

    if ano < 0:
        print(f"Digite um ano valido!")
    elif ano % 100 == 0:
        seculo = ano / 100
    elif ano % 100 != 0:
        seculo = (ano /100) + 1
    return seculo

seculo = descobrirSeculo()

def converterRomanos(seculo):
    algarismosRomanos = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }

    div = 1
    while seculo >= div:
        div *= 10

    div /= 10

    res = ""

    while seculo:
        ultimoNum = int(seculo / div)

        if ultimoNum <= 3:
            res += (algarismosRomanos[div] * ultimoNum)
        elif ultimoNum == 4:
            res += (algarismosRomanos[div] +
                    algarismosRomanos[div * 5])
        elif 5 <= ultimoNum <= 8:
            res += (algarismosRomanos[div * 5] +
                    (algarismosRomanos[div] * (ultimoNum - 5)))
        elif ultimoNum == 9:
            res += (algarismosRomanos[div] +
                    algarismosRomanos[div * 10])

        seculo = math.floor(seculo % div)
        div /= 10

    return res


# Driver code
print(f"O ano {ano} está no século {(converterRomanos(seculo))}")