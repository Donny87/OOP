""" Миксины """

# Mixin - классы, которые используются для дополнения функционала других классов путем наследова
# От миксинов нельзя создавать объекты


# class MicrowaveMixin:
#     def heat(self):
#         print('Я грею')

# class Fridge:
#     def cold(self):
#         print('Я охлаждаю')

# class TV:
#     def watch_tv(self):
#         print('Показываю фильм')

# class Cooker:
#     def cook(self):
#         print('готовлю еду') 



# class Kitchen(MicrowaveMixin, TV, Fridge, Cooker):
#     p = 10

# class BaseClass:
#     def eat(self):
#         pass

# class BaseMixin:
#     def eat(self):
#         print('я много ем')


# class ChildrenClass(BaseMixin, BaseClass):
#     pass

# obj = ChildrenClass()
# obj.eat()

# - При наследовании от миксинов и других классов - миксины нужно указывать в первую очередь (MRO)