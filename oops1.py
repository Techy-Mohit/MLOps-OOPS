# initiate a class
class Employee:
    #  special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")
# create an object/instance of the class
sam = Employee()
print(sam.designation)
sam.travel("New york")

print(type(sam))