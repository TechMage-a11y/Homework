x = int(input("Введите кол-во мальчиков: "))
y = int(input("Введите кол-во девочек: "))

if x > y * 2 or y > x * 2:
    print("Нет решения")
else:
    result = ""
    while x > 0 and y > 0:
        result += "BG"
        x -= 1
        y -= 1
    if x > 0:
        result += "B" * x
    elif y > 0:
        result += "G" * y
    print(result)