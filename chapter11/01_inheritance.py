class employee:
    com = "Sumago"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class programmer(employee):
    com = "Sumago Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def show_lang(self):
        print(f"The name is {self.name}and she is good with {self.language}")


a = employee()
b = programmer()

print(a.com, b.com)