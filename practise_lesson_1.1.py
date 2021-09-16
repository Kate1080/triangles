from math import sqrt
mas = [i for i in range(51, 0, -1)]
for i in range(1, len(mas) - 2):
    a = mas[i]
    b = mas[i + 1]
    c = mas[i + 2]
    if c + b > a:
        p = (a + b + c)/2
        s = sqrt(p * (p - a)*(p - b)*(p - c))
        print(s)
        break
