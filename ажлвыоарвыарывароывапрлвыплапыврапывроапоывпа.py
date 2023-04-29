a=open("привет.txt",'r')

textList = a.read().split()
print(textList)
a.close()