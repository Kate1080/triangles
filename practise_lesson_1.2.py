from math import sqrt
print("Введите размер массива - не меньше 3")
x = int(input())
print("Введите числа для массива")
mas = []
counter = 0
while counter < x:
    ch = int(input())
    if ch < 1:
        print("Число должно быть больше 0")
        continue
    else:
        mas.append(ch)
        counter += 1
mas.sort(reverse=True)
s = 0
for k in range(0, len(mas) - 2):
    a = mas[k]
    b = mas[k + 1]
    c = mas[k + 2]
    if c + b > a:
        p = (a + b + c) / 2
        s = sqrt((p * (p - a) * (p - b) * (p - c)))
        print(a, b, c)
        print(s)
        break
    else:
        continue
if s == 0:
    print("Невозможно составить треугольник")
