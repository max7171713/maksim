h = 0
a = [["*","*","*","*"],
     ["*","*","*","*"],
     ["*","*","*","*"],
     ["*","*","*","*"]]
for i in range(0,4):
    for j in range(0,4):
        h = int(input("введите число:"))
        a[i][j] = h
        print(a)
