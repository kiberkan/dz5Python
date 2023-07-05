a = int(input("Введите число "))
b = int(input("Введите степень числа "))
def exponentiation(a, b):
    if b == 0:
        return 1
    return a * exponentiation(a, b - 1)


print(exponentiation(a, b))