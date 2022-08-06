class Car():
    def __init__(self, color, prise, age, max_speed):
        self.color = color
        self.prise = prise
        self.age = age
        self.max_speed = max_speed
    
    def __str__(self):
        return 'Цвет машины - ' + self.color + '\nЦена машины - ' + str(self.prise) + '\nВозраст - ' + str(self.age)

    def __eq__(self, other) :
        if self.color == other.color:
            return True
        else:
            return False
    
    def __add__(self, other):
        color = 'black'
        prise = self.prise + other.prise
        age = self.age + other.age
        max_speed =self.max_speed + other.max_speed
        return Car(color, prise, age, max_speed)

car1 = Car('red', 1000000, 2, 180)
car2 = Car('red', 2000000, 32, 190)
car3 = car1 + car2
print(car3)
if car1 == car2:
    print('Одинаковые')
else:
    print('разные')
#print(car1)