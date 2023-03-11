n = int(input("напиши число"))
def foo(n) :
    a = 1
    if n ==1:
        return 1
    else:
        return a + foo(n-1)

print(foo(n))