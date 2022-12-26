from Employee import Employee


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.programming_language = programming_language


# dev_1 = Developer("Sam", "Oh", 12000, "Python")
# dev_2 = Developer("Akin1", "Bello", 24000, "C")

# print(dev_2.programming_language)

#print(help(Developer))