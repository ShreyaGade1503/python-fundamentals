class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

e = Employee()
e.a = 45

e.name = "John"
print(e.name)

e.show()