def updateValues(arr):
    
    value = []

    for i in range(1,len(arr),1):
        value = arr[1]

    for i in range(1,len(value),1):
        value[0] = 15


    return [arr[0],value]

def updateLastname(arr):
    
    students = []

    for i in range (0, len(arr), 1):
        students = arr[0]

    students['last_name'] = 'Bryant'
    
    return [students, arr[1]]

def updateSportDirectory():

    soccerPlayer = sports_directory['soccer']

    for i in range (0,len(soccerPlayer),1):
        soccerPlayer[0] = 'Andres'
    
    return soccerPlayer

def updateZValue(arr):

    z2 = []

    for i in range (0, len(arr), 1):
        z2 = arr[0]

    z2['y'] = 30

    return[z2]

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

x = updateValues(x)
print(x)

students = updateLastname(students)
print(students)

sports_directory['soccer'] = updateSportDirectory()
print(sports_directory)

z = updateZValue(z)
print(z)


#//////////////////////////////////////////////////////////////FUNCTION 2 ////////////////////////////////////////////////////////////////////////////////////////
def iterateDictionary(arr):

    for i in range (0, len(arr), 1):
            students = arr[i]
            print("first_name - "+ students['first_name']+", " "last_name - "+ students['last_name'])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#//////////////////////////////////////////////////////////////FUNCTION 3 ////////////////////////////////////////////////////////////////////////////////////////

def iterateDictionary2(key_name, some_list):

    data = []
    data = some_list[key_name]
    for i in range (0, len(data), 1):
            print(data[i])
        
students2 = {
            'first_name': [ 'Michael', 'John', 'Mark', 'KB', 'Bryan'],
            'last_name' : ['Jordan', 'Rosales', 'Guillen', 'Tonel', 'Cascante']
        }


iterateDictionary2('first_name', students2)
iterateDictionary2('last_name', students2)

#//////////////////////////////////////////////////////////////FUNCTION 4 ////////////////////////////////////////////////////////////////////////////////////////

def printInfo(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
