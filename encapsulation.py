""" Инкапсуляция 
1. Ограничения доступа к определенным данным
2. Объединение атрибутов и методов, которые работают с данными в один класс
"""
# Инкапсуляция в ПИТОНЕ реализованна на уровне соглашения


"""
Модификаторы доступа:
1. public 
Публичные атрибуты и методы доступные в классе, дочерних классах и вне класса 

2. protected
Защищенные атрибуты и методы доступны в классе, а также в дочерних классах, но при этом не доступны вне класса.

3. private
Приватные атрибуты и методы доступны только в том классе - где они определенны.
"""

from statistics import mode


class EncapsulatedClass:
    public = 'public'
    _protected = 'protected'
    __private = 'private'
    
    def pub_method(self):
        pass
    def _prot_method(self):
        pass
    def __priv_method(self):
        pass


enc = EncapsulatedClass()
# print(enc.public) # public
# print(enc._protected) # protected
# # print(dir(enc)) # AttributeError
# print(enc._EncapsulatedClass__private) # private


class InheritClass(EncapsulatedClass):
    pass

inh = InheritClass()

# print(inh.public) # public
# print(inh._protected) # protected
# print(inh._EncapsulatedClass__private) # private


""" setter & getter - интерфейсные методы """

class Light:
    __turned_on = False

    def __init__(self, brightness):
        self.__brightness = brightness


    # setter
    def set_status(self):
        self.__turned_on = True
    # getter
    def get_status(self):
        return self.__turned_on   

    @property # getter   
    def brightness(self):
        return self.__brightness

    @brightness.setter # setter
    def brightness(self, value):
        self.__brightness = value 


    # brightness = property(get_brightness, set_brightness)          




# lamp = Light(50) 
# # lamp._Light__turned_on = True # неправельный способ

# lamp.set_status()
# print(lamp.get_status()) # True
# print(lamp.brightness) # сработал get
# lamp.brightness = 70 # сработал set



class Car:
    __MAX_SPEED = 300
    __MIN_SPEED = 0

    def __init__(self, color, model,  max_speed, min_speed):
        self.color = color
        self.model = model
        self.max_speed = max_speed
        self.min_speed = min_speed
        if self.validate():
            raise ValueError('неправильно указанна скорость')

    def validate(self):
        return self.max_speed > self.__MAX_SPEED or self.min_speed < self.__MIN_SPEED    

car1 = Car('red', 'camry', 350, 0)

