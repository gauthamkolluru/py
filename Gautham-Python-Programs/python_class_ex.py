class Odometer():
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return self.size

    def make_sqr(self, name):
        self.name = name
        return self.size * self.size, self.name


o1 = Odometer(6)

o2 = Odometer(15)

print(o1.make_sqr('Gautham'))

print(type(o1))

print(o2.make_sqr('Sravani'))
