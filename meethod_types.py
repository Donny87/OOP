""" Виды методов """

# class MethodTypes:
#     class_attr = 'class_attr'
#     counter = 0

#     def __init__(self, obj_attr):
#         self.obj_attr = obj_attr

#     def instance_method(self):
#         return self.class_attr, self.obj_attr


#     @classmethod
#     def class_method(cls):
#         print(cls.class_attr)
#         print(cls.obj_attr) # AttrubuteError

#     @classmethod
#     def change_counter(cls):
#         cls.counter += 1    

#     @staticmethod
#     def static_method(x, y):
#         print('static method')
#         # cls.class_attr # Error
#         # self.obj_attr # Error
#         return x + y


# obj1 = MethodTypes(1)
# obj2 = MethodTypes(2)
# obj3 = MethodTypes(3)
# obj3.change_counter()
# obj1.counter = 10
# print(obj3.counter) # 10
# print(obj2.counter) # 0


class User:
    counter = 0

    def __init__(self, username, password):
        self.username = username
        self.password = self.encrypt_password(password)
        self.add_user()

    @staticmethod
    def encrypt_password(password):
        from hashlib import md5
        en_password = md5(password.encode()).hexdigest()
        return en_password    

    @classmethod
    def add_user(cls):
        cls.counter += 1    

   
user1 = User('StarBoy998', 'mysuperpassword 123')

print(user1.password)
print(user1.counter)



"""
1. instance method - обязательном порядке принимает self, имеют доступ к атрибутам класса, методам класса, к атрибутам экземпляра

2. classmethod - принимают cls -ссылка на класс - не имеют доступа к атрибутам экземпляра, но имеют доступ к атрибутам и методам класса

3. staticmethod - отдельная функция, которая не имеет доступа ни к классу, ни к объекту класса. Используется для дополнения функционала класса
"""

# a = {'a': 1, 'b': 2}
# a.update(c=3)
# dict.update(a, d=5)
# b = dict.fromkeys('asdf')
# print(b)