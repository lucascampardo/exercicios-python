nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
vendas = float(input("Digite seu vendas: "))

salario_final = salario + vendas * 0.15
salario_final = str("%.2f" % salario_final)


print("Total: ", salario_final)