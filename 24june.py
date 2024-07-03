
# # # # unpacking
# # # tup = (1,2,3)
# # # a,b,c = tup
# # # print(a)
# # # print(b)
# # # print(c)


# # # s= '' #empty string

# # # #sets-unique values and ;add or remove elements

# # # #set empty
# # # a= set()

# # # #set method-add not append
# # # #2 choti  add hudaina
# # # a= set()
# # # a.add('1')
# # # print(a)
# # # a.add

# # # lst = [1,1,2,3,3,4]
# # # a=set(lst)
# # # a.remove(3)#3 is removed
# # # print(a)

# # # #Discard in sets


# # # lst1 = [1,1,2,3,3,5,44]
# # # a=set(lst1)
# # # a.discard(3)#3 is removed
# # # print(a)

# # # #set ma vako value kasari update garne?


# # #| union

# # set1 = {1,2,3,4}
# # set2 = {3,4,5,6}

# # #Union
# # print(set1|set2)

# # #integration
# # print(set1 &set2)

# # #Difference
# # print(set1 - set2)

# # #Symmetric Difference 
# # print(set1 ^ set2)



# set1 = {'apple','ball','cat'}
# set2 = {'cat','banana'}

# #union
# print(set1 | set2)

# #integration
# print(set1 &set2)

# #Difference
# print(set1 - set2)

# #Symmetric Difference 
# print(set1 ^ set2)

# #Frozenset-immutable -cant add value - no method add works




# st = {1,2,3,4}
# a = frozenset(st)
# print(a)

#append add kasari garne is assignment

#Dictionary -Data types;empty dictionary 

#Empty dictionary
# empty_dict = {}

# #Dictionary with initial values
# my_dict = {
#     "name": "Alice",
#     "age" : 30,
#     "city" : "New York"

# }

# #Dictionary with mixed key types
# mixed_dict = {
#     1 :"one",
#     "2" : "two",
#     (1,2) : "tuple"
# }

# #2 wAys to access dictionary --> 1. large bracket , 2. get 

# #print(my_dict["name"])
# #print(my_dict.get("name1","Rohan"))

# my_dict["name"] = "rohan"
# #print("my_dict", my)


#.keys();.items()-key and value
#.len()-both values and keys
#.clear()-removes all the keys and values

#st ={1,2,3,4}

# my_dict = {
#     'name' : 'Alice',
#     'age': 30,
#     'city' :'New York'
# }

# #looping over keys
# for key in my_dict:
#     print(key , ':' , my_dict[key])


# student = {
#     'name': 'Alice',
#     'age':20,
#     'grades': {
#         'math' :90,
#         'history' :85,
#         'science' :95
#     },
#     'contact': {
#         'email' : 'alice@example.com',
#         'phone' : '123-456-7890'
#     }
# }
# print(student["grades"])

 

# print(student['grades']['math'])

# my_dict = {}
# my_dict["math"] = 90
# my_dict["science"] = 89

# print(my_dict)

# student = {}
# student["name"] = "rohan"
# student['grades'] = my_dict
# print(student)


# lst1 = []

# lst1.append(1)
# lst1.append(2)

# print(lst1)

# student["contact"]

# print(student)


# words  = ['apple','banana','cherry']
# word_lengths = {word : len(word) for word in words}

# print(word_lengths)






