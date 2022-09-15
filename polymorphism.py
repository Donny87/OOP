

""" Полиморфизм """

# Полиморфизм - принцип ООП, который заключается в использовании одной сущности(метод, оператор) для различных типов объектов.

# +

# num1 = 10
# num2 = 30
# print(num1 + num2) # сложение - 40

# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2) # конкатинация - HelloWorld


# class A:
#     def method1(self):
#         return 10 + 10 

# class B:
#     def method1(self):
#         return 'метод 1'

# objA = A()
# objB = B()
# for obj in (objA, objB):
#     print(obj.method1())



# class Cat:
#     def meow(self):
#         print('мяу')

# class Dog:
#     def bark(self):
#         print('гав')



# cat1 = Cat()
# dog1 = Dog()                

# for animal in (cat1, dog1):
#     if type animal is Cat:
#         animal.meow()

#     else:
#         animal.bark()    


""" Абстракция """

# абстракция - сущность без конкретной реализации

# class Animal:
#     def __init__(self):

#         self.eat()
#         self.sound()
#         self.move()

#     def eat(self):
#         raise NotImplementedError(self.__class__.__name__)


#     def sounf(self):
#         raise NotImplementedError(self.__class__.__name__)


#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)


# class Cow(Animal):
#     pass    


# cow = Cow()
# cow.eat()





# from abc import ABC, abstractmethod

# class AbstractClass(ABC):
#     def get_x(self):
#         return 'x'

#     @abstractmethod
#     def abs_method(self):
#         pass


# class ConcreteClass(AbstractClass):
#     def method1(self):
#         print(12121) 

#     def abs_method(self):
#         return 'Hello world!'    

# obj = ConcreteClass()               
