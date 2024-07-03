# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         return f"Hello , my name is {self.name} and I am {self.age} years old"

# person1 = Person("Alice",39)
# person2 = Person("bob",25)

# print(person1.name)
# print(person1.age)

# message = person1.greet()
# print(message)

# class Person:
#     a=10
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self,address):
#         return f"hello,my name is {self.name} and I am {self.age} years old. I live in {address}"
    
#     def gender(self,gen):
#         return f"gender :{gen}"
    
# person1 = Person("alice",30)
# person2 = Person("bob",25)
# person3 = Person("bob123",15)

# print(person2.name)
# print(person2.age)
# message  = person1.greet("lalitpur")
# print(message)
# gend = person1.gender("male")
# print(gend)

# class Animal:
#     def speak(self):
#         return "Animal speaks"

# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"

# my_dog = Dog()
# print(my_dog.speak())
# print(my_dog.bark())

# class A:
#     def method_A(self):
#         return "Method A"

# class A:
#     def method_B(self):
#         return "Method B"
# class C(A,A):
#     def method_C(self):
#         return "Method C"

# obj_c = C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())

# class A:
#     def method_A(self):
#         return "Method A"

# class B(A):
#     def method_B(self):
#         return "Method B"

# class C(B):
#     def method_C(self):
#         return "Method C"

# obj_c= C()
# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_A())

class Rectangle:
    def __init__(self, length, width):
        self.length =length
        self.width = width
    
    def area(self):
        return self.length *self.width
    
class Square(Rectangle):
        def __init__(self,side_length):
            super().__init__(side_length,side_length)
    
    rectangle = Rectangle(5,3)
    square = Square(4)

    print("Area of Rectangle ", rectangle.area())
    print("Area of Square", square.area())