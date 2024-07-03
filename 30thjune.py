# #FILE HANDLING
# with open('sample.txt','r') as file:
#     a =file.read()
#     print("reading the file content")
#     print(a)

with open("sample.txt","a+") as file:
    a=file.write()
    print("open a text file for both reading and writing without truncating it.")
    print(a)

# with open("sample.txt","a+") as file:
#     a=file.read()
#     print("append")
#     print(a)

# with open("sample.txt","w+") as file:
#     a=file.read()
#     print("write")
#     print(a)

# with open("sample.txt","wb+") as file:
#     a=file.read()
#     print("write binary")
#     print(a)

# with open("sample.txt","ab+") as file:
#     a=file.read()
#     print("appenddddd")
#     print(a)


#all mode ma + use garyo bhane k huncha is assignmnet ,read+,write+ and append+,binary+ pani herne

# with open('sample.txt','w') as file:
#      a =file.write("I am writing \t to the \n file") #tab and new line 
#      print("reading the file content")

# with open("sample.txt",'r') as file:
#     a = file.readlines()
#     print(a)
#     lst = []
#     for x in a:
#         value = x.strip('\n')
#         print(value)
#         lst.append(value)

#     print("newlist",lst)


# file = open('sample.txt' ,'r')
# a = file.read()
# print(a)
# file.close()

# file_path = 'sample.txt'
# with open(file_path, 'a') as file:
#     file.write("Appending new line!\n")

# file_path = 'sample.txt'
# with open(file_path, 'w') as file:
#     file.write("Hello, world!\n")

# with open("sample.txt",'r') as file1, open("sample4.txt",'w') as file2:
#     a = file1.readlines()
#     print(a)
#     lst = []
#     for x in a:
#         value = x
#         print(value)
#         lst.append(value)

#     file2.writelines(lst)

# try :
#     with open("sample.txt",'r') as file1, open("sample5.txt",'r') as file2:
#         a = file1.readlines()
#         print(a)
#         lst = []
#         for x in a:
#             value = x
#             print(value)
#             lst.append(value)

#         file2.readlines()

# except FileNotFoundError:
#     print("one of the file doesn't exist")

    
# import csv

# file_path = "data.csv"

# with open(file_path, mode = 'r') as file:
#     csv_reader = csv.reader(file)
#     header = csv.reader(file)
#     for row in csv_reader:
#         print(row)

# import csv

# data = [
#     ['Alice', 30, 'London'],
#     ['Bob',25, 'Paris'],
#     ['Charlie',35,'Berlin']
# ]

# file_path = 'output.csv'
# with open(file_path, mode= 'w',newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name','Age','City'])
#     for row in data:
#         csv_writer.writerow(row)

# import csv

# file_path = 'data.csv'

# with open(file_path, mode='r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row['Name'],row['Age'],row['City'])

# import csv

# data = [
#     {'Name':'Alice','Age':30,'City':'London'},
#     {'Name':'Bob','Age':25,'City':'Paris'},
#     {'Name':'Charlie','Age':35,'City':'Berlin'}
# ]

# file_path = 'output.csv'
# fieldnames = ['Name','Age','City']

# with open(file_path,mode = 'w',newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)




# homework

#r+-open a text file for both reading and writing without truncating it. 
# rb+: Same as r+, but for binary files.
# w+: Allows both reading and writing; creates a new file if it does not exist or truncates the file if it exists.
# wb+: Same as w+, but for binary files.
# a+: Allows both reading and writing; creates a new file if it does not exist. Data is appended to the end of the file if it exists.
# ab+: Same as a+, but for binary files.