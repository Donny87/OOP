# class MyDict(dict):
#     def get(self,key, default = 'Are you kidding?'):
#         return super().get(key, default)

# obj_dict = MyDict({'Some_shit': 3})        
# print(obj_dict.get('some'))


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)    

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(self.name, self.age, self.faculty)    


# obj_student = Student('Rick', 21, 'science')

# obj_student.display()
# obj_student.display_student()


# class ContactList(list):
#     def __init__(self, value = list()):
#         self.value = value


#     def search_by_name(self, name):
#         result = []
#         for elem in self.value:
#             if name in elem:
#                 result.append(elem)
#         return result        
        



# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))               

# class Smartphones(str):
#     battery = 0
#     def __init__(self, name, color, memory, battery):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def str(self):
#         print(f"{self.name},{self.memory}")


#     def charge(self, value):



# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km
#         result = self.cost + self.cost_km * self.km
#         return f'Такси {self.name}, стоймость поездки: {result} сом' 

# taxi1 = Taxi('Namba', 60, 15)
# taxi2 = Taxi('Yandex', 60, 10)
# taxi3 = Taxi('Jorgo', 70, 12)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))


# class ContactList(list):
#     def __init__(self, value = list()):
#         self.value = value


#     def search_by_name(self, name):

            
            
        
#         list_ = []
#         for elem in self.value:
#             if name in elem:
#                 list_.append(elem)
#         return list_        



        


# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))


# class Dog:
#     def voice(self):
#         return('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')


# barsik = Cat()

# rex = Dog()

# def to_pet(animal):
#     animal.voice()
   

# to_pet(barsik) 
# to_pet(rex) 



from unicodedata import name


# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name 

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'    




# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}.'




# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе.'



# def get_human_info(obj):
#     print(obj.get_info())






# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров', 'компании Рога и копыта', 'директор')
# student = Student('Иван', 'Петров', 'КГТУ', '3 курсе')  


# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 