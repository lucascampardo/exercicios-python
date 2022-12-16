a, b = map(int, input("Digite dois números:\n").split())

if a % b == 0 or b % a == 0:
    print("São multiplos")
else:
    print("Não são multiplos")