f = open("c.txt","r",encoding="utf-8")
h = 0
for line in f:
    h = h+1
f.close()
print(h)