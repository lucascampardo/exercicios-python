nota_um = float(input("Insira a nota do primeiro bimestre: "))
nota_dois = float(input("Insira a nota do segundo bimestre: "))
nota_tres = float(input("Insira a nota do terceiro bimestre: "))
nota_quatro = float(input("Insira a nota do quatro bimestre: "))
media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4
media = str("%.1f"%media)

print("Media: ", media)

