qtpessoas = 10
idademulheres = []
idadehomens = []
idadegrupo = []

for a in range(qtpessoas):

    print(f"Digite a idade {a + 1}: ")
    idade = int(input())

    print(f"Digite o sexo da pessoa {a + 1} (M ou F): ")
    sexo = input().upper()

    if sexo == 'F':
        idademulheres.append(idade)
    elif sexo == 'M':
        idadehomens.append(idade)

    idadegrupo.append(idade)

media_mulheres = sum(idademulheres) / len(idademulheres)
media_homens = sum(idadehomens) / len(idadehomens)
media_grupo = sum(idadegrupo) / qtpessoas

print(f"A média de idade das mulheres é: {media_mulheres}")
print(f"A média de idade dos homens é: {media_homens}")
print(f"A média de idade do grupo é: {media_grupo}")