start = float(input("Введите начало отрезка: "))
end = float(input("Введите конец отрезка: "))
step = float(input("Введите шаг (отрицательный): "))

if step > 0:
    step = -step

if start > end:
    start, end = end, start

x = end
while x >= start:
    y = x**3 + 2*x**2 - 4*x + 1
    print(f"x = {x:.2f}, y = {y:.2f}")
    x += step