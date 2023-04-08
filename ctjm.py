class Slimea:
    def __init__(self,a,b,c,d):
        self.name = a
        self.rost = b
        self.ves = c
        self.color = d
    def ispug(self, otherSlime):
        if self.ves>otherSlime.ves:
            return True
        else:
            return False
    

slime2 = Slimea("Круг", 72, 21, "синий")
slime1 = Slimea("Круг", 74, 222, "синий")
print(slime1.ves)
print(slime2.ves)
if slime1.ispug(slime2):
    print("прив я", slime1.name, "мой рост в метрах", slime1.rost, "мой вес", slime1.ves, "я цвета", slime1.color)