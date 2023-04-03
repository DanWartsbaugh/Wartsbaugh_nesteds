students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    
def iterateDictionary(students):
    for student in range(len(students)):
        first = students[student]["first_name"]
        last = students[student]["last_name"]
        print(f"first_name - {first}, last_name - {last}")
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for item in range(len(some_list)):
        print(some_list[item][key_name])

iterateDictionary2('last_name',students)

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
