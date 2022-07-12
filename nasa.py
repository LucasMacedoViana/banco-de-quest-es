asteroide = {}
while True:
    distancias = []
    nome_asteroide = input("Digite o nome do asteroide: ")

    for i in range(5):

        in_distancia = float(input(f"Digite a {i + 1}ª distancia do asteroide: "))
        distancias.append(in_distancia)
        asteroide.update({nome_asteroide: distancias})
    parar = input("\n(s) para inserir novo asteroide"
                  "\n(n) para não inserir outro asteroide"
                  "\nDeseja inserir outro asteroide?: ")

    if parar == 's':
        continue
    elif parar == 'n':
        break

for nome_asteroide in asteroide:
    media = sum(asteroide[nome_asteroide])/5
    print(f"a distâcia media do asteroide {nome_asteroide} é de {media}Km")



