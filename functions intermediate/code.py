x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# def iterateDictionary(some_list):
#     index = 0
#     for index in range(len(some_list)):
#         for key in some_list[index]:
#             print(some_list[index][key])

# iterateDictionary(students)

# def iterateDictionary2(key_name, some_list):
#     for i in range(0,len(some_list)):
#         for key,val in some_list[i].items():
#             if key==key_name:
#                 print(val)


# iterateDictionary2('first_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])


printInfo(dojo)