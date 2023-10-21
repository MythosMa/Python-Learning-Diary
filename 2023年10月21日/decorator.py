import datetime

class Person:

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return datetime.date.today().year - self._birth
    
a = Person()
a.birth = 1988
print(a.age)
