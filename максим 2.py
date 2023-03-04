n = int(input("напишите число 1"))
b = int(input("напишите число 2"))
def equality (n,R):
    if n<R:
        print(n)
        equality(n + 1,R)
    if n>R:
        print(n)
        equality(n - 1,R)
equality(n,b)