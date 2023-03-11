n = int(input("напиши число"))
a = 2
def foo(n,a) :
    if n == a:
        print("YES")
    elif n > a:
        return foo(n, a * 2)
    elif n < a:
        print("NO")

print(foo(n,a))