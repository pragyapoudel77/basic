# from abc import ABC, abstractmethod

# class Car(ABC):
#     def __init__(self, brand, model ,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# @abstractmethod
# def printDetails(self):
#         pass


# def accelerate(self):
#      print("speed up..")

# def break_applied(self):
#      print("Car stop")

# class Hatchback(Car):
     
#      def printDetails(self):
#           print("Brand:",self.brand)
#           print("Model",self.model)
#           print("Year",self.year)

#      def Sunroof(self):
#           print("Not having this feature")
    
# class Suv(Car):
     
#      def printDetails(self):
#           print("Brand:",self.brand)
#           print("Model",self.model)
#           print("Year",self.year)

#      def Sunroof(self):
#           print("Available")
# car1 = Hatchback("MAruti","Alto","2022")
# car1.printDetails()



#-------------------

#AccessModifier#

# class MyClass:
#     def __init__(self):
#         self.__private_var = "Private attribute"

#     def __private_method(self):
#         return "This is a private method"
    
# obj = MyClass()

# print(obj._MyClass__private_var)
# print(obj._MyClass__private_method())

# class Animal:
#     def make_sound(self):
#         print("Some generic sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# dog = Dog()
# cat = Cat()

# dog.make_sound()
# cat.make_sound()
