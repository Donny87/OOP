""" Множественное наследование """

from multiprocessing.util import close_all_fds_except


class Dad:
    eyes = 'green'
    hair = 'black'


class Mom:
    hair = 'brown'
    eyes = 'blue'

class Child(Dad, Mom):
    pass

child = Child()

print(child.eyes) # green
print(child.hair) # brown

""" Поиск атрибутов и методов идет слева направо """

# class.mro() - метод для получения списка порядка поиска методов и атрибутов - method resolution order

# print(Child.mro()) # [<class '__main__.Child'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class 'object'>]

""" Проблема ромба """
# class A:
#     def method(self):
#         print(A.__name__)


# class B(A):
#     def method(self):
#         print(B.__name__)


# class C(A):
#     def method(self):
#         print(C.__name__)        


# class D(B, C):
#     def method(self):
#         # super().method() #  обращение к родителю
#         A.method(self) # -делегирование
#         print(' D method')

# obj = D()
# obj.method()
# print(D.mro())

""" перекрестное наследование (не решено) """
# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass


# class E(C, D):
#     pass



 #-----------------------------------------------

# SOLID
# S - single responsibility
# O - open-closed 
# L - Liskov substitution
# I - Interface segregation
# D - Dependency inversion


""" S """
# class DateTemp:
#     def date(self):
#         print('сейчас 3 часа')

#     def temp(self):
#         print('сейчас 38 градусов')

# class Date(DateTemp):           --------------------  НЕПРАВИЛЬНО
#     pass

# class Temp(DateTemp):
#     pass




# class Date:
#     def time(self):
#         print(' now 4pm')

# class Temp:
#     def temp(self):
#         print(' now 30 degrees') -------------------- ПРАВИЛЬНО


# class DateTemp(Date, Temp):
#     pass        
