print("--- CALCULADORA DE MÉDIA (PYTHON) ---")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média final é: {media:.2f}")

if media >= 6:
    print("Status: Aprovada! 🚀")
else:
    print("Status: Recuperação. ✨")