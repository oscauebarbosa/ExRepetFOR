homemOld = " "
idadeHomemOld = 0
mulherMenos20 = 0


for i in range(3):
    nome = input(f'Digite o nome da pessoa {i+1}: ')
    idade = int (input(f'Digite a idade da pessoa {i + 1}: '))
    sexo = input(f'Digite o sexo da pessoa {i + 1} (M ou F): ')

    if sexo.upper() == "M" and idade > idadeHomemOld:
        homemOld = nome
        idadeHomemOld = idade

    if sexo.upper() == "F" and idade < 20:
        mulherMenos20 += 1

print(f"\nO homem mais velho é {homemOld}")

if mulherMenos20 == 1:
    print("Existe 1 mulher com menos de 20 anos")
else:
    print(f"\nExistem {mulherMenos20} mulheres com menos de 20 anos")




