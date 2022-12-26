from Developer import Developer
from Manager import Manager

dev_1 = Developer("Samuel", "Ohiri", 12000, "Python")
dev_2 = Developer("Akin1", "Bello", 24000, "C")

mgr_1 = Manager("Jules", "Okato", 36000, [dev_1])
mgr_1.add_employee(dev_2)

mgr_1.print_employees()

print(mgr_1.email)
print(dev_1.email)