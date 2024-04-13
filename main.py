def encontrar_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encontrar_mcm(a, b):
    return (a * b) // encontrar_mcd(a, b)

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

mcd = encontrar_mcd(num1, num2)
mcm = encontrar_mcm(num1, num2)

print("El máximo común divisor de", num1, "y", num2, "es:", mcd)
print("El mínimo común múltiplo de", num1, "y", num2, "es:", mcm)
