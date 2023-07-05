a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))
def sum_numbers(a, b):
    if a == 0:
        return b
    else:
        return sum_numbers(a - 1, b + 1)

print(sum_numbers(a, b))