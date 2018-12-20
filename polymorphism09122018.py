class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
    
    def name(self):
        return self.fn+self.ln

class Employee(Person):
    def __init__(self,fn, ln, en):
        # Person.__init__(self,fn,ln)
        super().__init__(fn,ln)
        self.en = en
    
    def ed(self):
        self.name = Person.name(self)
        return self.name+str(self.en)

p1 = Person('Django','Python')

p2 = Employee('Flask','Python',3.7)

print(p1.name())
print(p2.ed())