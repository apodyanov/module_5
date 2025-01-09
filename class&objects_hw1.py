class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        f = self.number_of_floors
        n = new_floor
        for i in range(1, n+1):
            if 2 <= n <= f:
                print(i)
            else:
                print("Такого этажа не существует")
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)