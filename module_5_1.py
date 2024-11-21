class House:
    def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = number_of_floors
         # return (self.number_of_floors)

    def go_to(self, floor):
        from time import sleep
        if floor < self.number_of_floors or floor < 1:
            for num in range(1, floor + 1):
                sleep(0.5)
                print(num)
        else:
            sleep(1)
            print(f'В "{self.name}" такого этажа ({floor}) не существует.')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
