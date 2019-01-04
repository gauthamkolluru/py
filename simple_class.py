class Customer:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("I am, ", self.name)


c = Customer("Gautham")

c.display()

c.address = "jingalala"

print(c.address)
