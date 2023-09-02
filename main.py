class House:
    def __init__(self, name, num):
        self.number = int(num)
        self.hName = name

    def notify(self):
        print("House Namer " + self.hName + "\nRoom Number " + str(self.number))


print("Notifying")
house1 = House("010", 543)
house1.notify()
