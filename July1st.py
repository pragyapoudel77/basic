#others

# square = lambda x: x ** 2
# print(square(5))


# add = lambda a,b: a + b
# print(add(3,4))

# square = lambda x:x+x
# print(square(9))

# lambda -small anonymous function

# lst = [1,2,3,4,5]
# def fun(a):
#      a =a+1
#      return a

# inc = list(map(fun,lst))
# print(inc)

# numbers =[1,2,3,4,5]

# squared = list(map(lambda x: x**2, numbers))

# print(squared)


#filter

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers =list(filter(lambda x: x % 2 == 0,numbers))
# print(even_numbers)

# def is_even(x):
#     return x %2 ==0

# numbers = [1,2,3,4,5,6,7,9,10]

# even_numbers = list(filter(is_even,numbers))

# print(even_numbers)

# from functools import reduce

# numbers = [1,2,3,4,5]

# summing up a list of numbers
# sum =reduce(lambda x,y :x+y, numbers)
# print(sum)


# #maximum number in a list
# numbers = [3,8,1,6,2]
# max_num = reduce(lambda x,y:x if x>y else y,numbers)
# print(max_num)

# #Concatenating strings in a list
# words = ["Hello", " ","World", "1"]
# sentence = reduce(lambda x,y :x+y,words)

# #using an initializer
# numbers = [1,2,3,4,5]
# product=reduce(lambda x,y: x*y, numbers,1)
# print(product)

# #instead of lambda use fun mathiko


# import os

# #get current working directory

# current_dir = os.getcwd()
# print(current_dir)

# # #list files in a directory

# files = os.listdir(current_dir)
# print(files)


# #get current working directory
# current_dir = os.getcwd()
# print("Current Directory", )

#create anew directory
# new_dir = "new directory1"
# os.mkdir(new_dir)
# print(f"Created Directory'{new_dir}'")

# #check if a path is a directory or file
# path_to_check = new_dir
# if os.path.isdir(path_to_check):
#     print(f"{path_to_check} is a directory")
# elif os.path.isfile(path_to_check):
#     print(f"{path_to_check}is a file")
# else :
#     print(f"{path_to_check} is neither a file nor a directory")

# #change directory
# os.chdir(new_dir)
# print("changed current durectory to:",os.getcwd())

# #list files and directories in the new directory
# new_dir_files = os.listdir()
# print("Files and Directories in the new directory:", new_dir_files)

#import random

# random_number = random.randint(1,10)
# print(random_number)

# my_list = [1,2,3,4,5]
# random.shuffle(my_list)
# print(my_list)

# print("randomddsfsd ",random.choice(["apple","banana","cherry"]))

# population = range(1,11)
# sample = random.sample(population,5)
# print("Random sample from population",sample)

# import math

# sqrt_value = math.sqrt(25)
# print(sqrt_value)

# factorial_value = math.factorial(5)
# print(factorial_value)

#trigonometric functions

# print("sin(pi/2):", math.sin(math.pi / 2))

# print("exp(1):" , math.exp(1))
# print("2^3:",math.pow(2,3))

from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x + y ,numbers)
print(sum)

#qn1
def sum():
    numbers = [1,2,3,4,5]
    numberssum =numbers[0] +numbers[1]+numbers[3]+numbers[2]+numbers[4] 
    return numberssum
    
print(sum())




def sum12():
    sum10 = 0
    numbers2 = [1,2,3,4,5]
    
    for number10 in numbers2:
         sum10 = sum10+number10   
    return sum10   

print(sum12())






        # number = number 

        #qn2.

numbers1 = [3,8,1,6,2]
max_num = reduce(lambda x,y:x if x>y else y,numbers)
print(max_num)



def maximum_number10():
    numbers20 =[3,8,1,6,2]
    y = max(numbers20)
    return y
        
print(maximum_number10())



# def maximum_number10():
#     numbers20 =[3,8,1,6,2]
    

# qn2 answers

words = ["Hello"," ","world","!"]
sentence = reduce(lambda x, y:x+y,words)
print(sentence)




def word10():
    words1 = ["Hello"," ","world","!"]
    
    sentence1 = ""
    for worda in words1:
        print(worda)
        sentence1=sentence1 + worda
    return sentence1
        
print(word10())

from functools import reduce

# Define a function to concatenate two strings
def concat(x, y):
    return x + y

words = ["Hello", " ", "world", "!"]
sentence = reduce(concat, words)
print(sentence)




numbers = [1,2,3,4,5]
product = reduce(lambda x,y:x*y,numbers,1)
print(product)

#qn ---------

def num():
    numberrs = [1,2,3,4,5]
    product1 = 1
    for num2 in numberrs:
        product1 = num2 * product1
    return product1
print(num())
    


prod = 1  
numb=[1,2,3,4,5]
def mul(numb,prod):
    return numb*prod

result10 = reduce(mul,numb)
print(result10)
    



