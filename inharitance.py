# DRY - Don't Repeat Yourself

""" Наследование - это процесс, когда один класс происходит от другого класса """


# class Parent: # родительский(базовый) класс, base
#     pass

# class Child(Parent): # дочерний(производный) класс, chhild, inherated
#     pass



# class Parent:
#     hands = 2
#     eyes = 2

#     def draw(self):
#         print('Родитель хорошо рисует')

# class Child(Parent):
#     pass


# ch =Child()
# ch.draw() # - Родитель хорошо рисует

""" При наследовании дочерние классы перенимают все атрибуты и методы родительского класса """

# class Animal:
#     def sound(self):
#         print('Животоное издает звук')
    
#     def run(self):
#         print('Животное бежит')



# class Cat(Animal):
#     def sound(self):
#         print('Мяу')
        
        # """ Переопределение метода - полное изменение поведения метода """


# class Dog(Animal):
#     def run(self): # дополнение метода
#         super().run()
#         print('Собака бежит')

        # """ super() - функция для обращения к родительскому классу """


# cat = Cat()
# dog = Dog() 
# cat.sound()
# dog.run()       



# class A:
#     attr1 = 10

#     def mul(self):
#         return self.attr1 * 2


# class B(A):
#     attr2 = 10

#     def mul(self):
#         par = super().mul()
#         return par + self.attr2


# obj = B()
# print(obj.mul()) # 30                



""" Наследоваться можно от встроенных классов """

# class MyStr(str):
#     def first(self):
#         return self[0]

#     def last(self):
#         return self[-1]


#     def upper(self):
#         print('Переведенно в верхний регистр')
#         return super().upper()
        

# str1 = MyStr('Makers')

# str1.first() # h
# str1.last() # o
# str1.upper() # MAKERS


# print(issubclass(MyStr, str)) # True

from re import A


# class Person:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, last_name, age, course, faculty):
#         super().__init__(name, last_name, age)
#         self.course = course
#         self.faculty = faculty


# p = Person('Malik', 'Davletov', 24)
# print(dir(p))                

# object --> Person --> Student

""" множественное наследование """

# class A:
#     def method1(self):
#         print('метод А')

# class B:
#     def method2(self):
#         print('метод B')        

# class C(A, B):
#     pass        

# obj = C()

# obj.method2()

