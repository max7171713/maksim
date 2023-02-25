def foo(a):
    n = []
    
    for i in range(len(a)):
        d=True
        for j in range(len(a)):
            if a[i]==a[j] and i!=j:
                d=False
        if d == True:
            n.append(a[i])
    print(n)
b=[5,9,3,8,2,0,2,3,9]
foo(b)
    