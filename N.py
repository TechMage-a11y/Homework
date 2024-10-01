N = int(input("Введите число: "))
sum = 0
for n in range(N):
    elem = (-1) ** n * (1 / (2 ** n))
    sum += elem
print(f"Сумма из {N} элементов равна: {sum}")