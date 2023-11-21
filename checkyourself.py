"""TASK 1"""

import datetime
class CreateMixin:
    def create(self, todo, key):
        if key in self.todos.keys():
            return "Задача под таким ключом уже существует"
        else:
            self.todos.update({key:todo})
            return self.todos 
class DeleteMixin:
    def delete(self, key):
        popped = self.todos.pop(key)
        return f'удалли {popped} задачу'
class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos
class ReadMixin:
    def read(self):
        list_ = []
        for i,j in self.todos.items():
            list_.append((i, j))
        return list_
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, deadline):
        now = datetime.datetime.now()
        now = now.strftime('%d/%m/%Y')
        now = now.split('/')
        list_ = deadline.split('/')
        date1 = datetime.datetime(year=int(list_[-1]), month=int(list_[1]), day=int(list_[0]))
        date2 = datetime.datetime(year=int(now[-1]), month=int(now[1]), day=int(now[0]))
        lendays = str(date1 - date2)
        lendays = lendays.split(' ')
        lendays = lendays[0]
        return lendays



"""TASK 2"""

class Person:
    def __init__(self, name=None, last_name=None, age=None, email=None):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        self.__email = new_email

john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com



"""TASK 3"""


class Dog:
    def voice(self):
        return 'Гав'
    
class Cat:
    def voice(self):
        return 'Мяу'
    
def to_pet(animal):
    print(animal.voice())
barsik = Cat()
rex = Dog()
to_pet(barsik)
to_pet(rex)