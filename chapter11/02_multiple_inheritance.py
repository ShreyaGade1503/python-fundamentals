class employee:
    com = "Sumago"
    name = "Anjali"
    salary = 50000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and company is {self.com}")

class coder:
    lang = "Python"
    def language(self):
        print(f"The name is {self.name} and she is good with {self.lang}")

class programmer(employee, coder):
    comp = "Sumago Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def show_lang(self):
        print(f"The name is {self.name}and company is  {self.comp}")


a = employee()
b = programmer()

print(a.com, b.com)

b.show()
b.language()
b.show_lang()