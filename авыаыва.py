l = 0
m = 0
n = 0
a = int(input("любое число"))
b = int(input("любое число"))
for l in range(10):
    if a % 2 == 0:
        print("число четное")
        a = int(input("любое число"))
        n = n+a
    else:
        print("число нечетное")
        a = int(input("любое число"))
        m = m+a
    if b % 2 == 0:
        print("число четное")
        b = int(input("любое число"))
        n = n+b
    else:
        print("число нечетное")
        b = int(input("любое число"))
        m = m+b
print("это сумма не четных чисел",m)
print("это сумма не четных чисел",n)
