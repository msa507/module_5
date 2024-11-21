class House:
    def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = number_of_floors
         return (self.number_of_floors)

    def go_to(self, floor):
        if floor < self.number_of_floors or floor < 1:
            print(floor)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
