class Employee:
    company = "Google"


Yash = Employee()

Puneet = Employee()
Puneet.company = "Oracle"
print(Yash.company)

print(Puneet.company)
