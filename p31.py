# We alawys use self whenever we use function inside a class

class Employee:
    company = "Google"
# self is a paramter which gets automatically passed whenever we call any object

    def getSalary(self):
        print(f"Salary is {self.salary}")


Yash = Employee()
Yash.salary = 100000000

Yash.getSalary()

print(Yash.company)
