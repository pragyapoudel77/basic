#Type Validation

# value = input("Enter a number")

# if value.isdigit():
#     num = int(value)
#     print(f"Converted to integer:{num}")

# elif '.' in value:
#     num = float(value)
#     print(f"Converted to float:{num}")

# else:
#     print("Invalid number input")


# number = float(input("Enter a number"))

# if number>0:
#     print("Positive number")

# elif number<0:
#     print("Negative number")

# else:
#     print("zero")


# fruit=str(input("Enter a fruit:"))

# if fruit == 'apple':
#     print("apple")
# elif fruit == 'mango':
#     print('mango')
# else:
#     print("neither mango nor apple")

# x=10
# if x>5:
#     print("x is greater than 5")

# if x<15:
#     print("x is less than 15")

# x=4
# if x<5:
#     x+=20
#     print("x is greater than 5")

# if x>15:
#     print(f"x is less than 15 {x}")

#Nested Conidtionals

# x=5
# if x>0:
#     if x<10:
#         print("x is a posistive single-digit number")
#     else:
#         print("x is a positive number but not a single-digit")
# else:
#     print("x is not a positive number")

# nam - "dsfdsf"    

# if nam.isdigit() and nam > '5' or nam <10:
#         number = int(nam)
#         print(number)a


# val = int(name)

# if val.isdigit() and val >5 or val < 10:
#     print(number)

# fruits = "mango"
# value = fruits*2
# print(value)

# fruits = ["mango","apple","orange","grapes"]
# value = fruits*2
# print(value)

# fruits = ("mango","apple","orange","grapes")
# value = fruits*2
# print(value)

# value = input("Enter a number")

# if value.isdigit():
#     num = int(value)
#     print(f"Converted to integer: {num}")
# elif '.' in value:
#     num = float(value)
#     print(f"Converted to float: {num}")
# else:
#     print("Invalid number input")


#iterating over a list

# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num)

# stringwords = "pragya","ram","aman"
# for word in stringwords:
#     if word =="pragya":
#         print(word)
#     else:
#         print("other word",word)

#dictionary iteration
# val = {"name": "Pragya","address":"tilganga"}

# for key,values in val.items():
#         print("this is key",key)
#         print("this is values",values)


# for a in range(10):
#         print("range", a)

# lst = [1,2,3,4,5,6]
# length = len(lst)
# print("length of list", length)

# for a in range(4,10):
#         print("range", a)

count = 0
while count <5:
    print(count)
    count +=1

    #     print(num)
    # else:
    #     print("other numbers",num)
