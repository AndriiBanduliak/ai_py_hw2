a = int(input("Введите число: "))
c = 0
if a > 0 and a <= 10**4:
    s = (a + 1) * a / 22
elif a < 0 and a > (-1) * 10**4:
    s = (a - 1) * a / 2 * (-1)
print(f'Cумма целых чисел от 1 до {a}  равна "',int(s), '"')