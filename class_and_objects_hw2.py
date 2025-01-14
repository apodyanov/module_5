# Задача "Магические здания"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        f = self.number_of_floors
        n = new_floor
        for i in range(1, n+1):
            if n <= f:
                print(i)
            else:
                print("Такого этажа не существует")
                break


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1.__str__()
h2.__str__()

print(len(h1))
print(len(h2))