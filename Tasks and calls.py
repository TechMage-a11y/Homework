import random

tasks_count = 0
phone_calls = 0

for i in range(8):
    tasks_count += random.randint(1, 5)

print(f"За день Максим выполнил {tasks_count} задач.")

phone_calls = random.randint(0, 1)
if phone_calls > 0:
    print("Ему нужно зайти в магазин")
elif phone_calls == 0:
    print("Ему не нужно зайти в магазин")