min_overall_score = 210
math_score = int(input("Введите баллы по математики: "))
biology_score = int(input("Введите баллы по биологии: "))
russian_score = int(input("Введите баллы по русскому: "))
overall_score = math_score + biology_score + russian_score
if overall_score >= min_overall_score:
    print("Вы поступили")
else:
    print("Вы не поступили")

print("Общее количество баллов:", overall_score)