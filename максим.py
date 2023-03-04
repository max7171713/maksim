n = int(input("напишите число"))
def equality (n,R):
    if n != R:
        print(n)
        equality(n + 1,R)
equality(1,n)