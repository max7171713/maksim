a = input("Введите слово")
b = 0

for a in a:
    if a.lower() == "о":
        b += 1

print("В слове",a,b,"букв(ы/a) о")