x = [[5, 2, 3], [10, 8, 9]]

# How would you change the value 10 in x to 15?
# Once you're done x should then be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
# students[0]['first_name'] = 'Bryant'
# print(students)


sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

# For the sports_directory, how would you change 'Messi' to 'Andres'?
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

z = [{'x': 10, 'y': 20}]

# For z, how would you change the value 20 to 30?
# z[0]['y'] = 30
# print(z)

students2 = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDic(dic):
    for i in dic:
        dictString = ""
        for (k, v) in i.items():
            dictString += f'{k} - {v} '
        print(dictString)
        dictString = ""


# iterateDic(students2)

def iterateDic2(key, dic):
    for i in dic:
        for (k, v) in i.items():
            if k == key:
                print(v)


# iterateDic2('first_name', students2)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printDojoInfo(dic):
    for (k, v) in dic.items():
        count = len(v)
        print(f'{count} {(k).upper()}')
        for a in v:
            print(a)


# printDojoInfo(dojo)

# python swap
arr = [1, 3, 5, 7]
# swaps first and second values of the array
arr[0], arr[1] = arr[1], arr[0]

# print(arr)
