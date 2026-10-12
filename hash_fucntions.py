HASH_TABLE_SIZE = 100000
hash_table = [[] for i in range(HASH_TABLE_SIZE)]


student_1 = {
    'name': 'Cole',
    'age': 15,
    'grade': 10
}
student_2 = {
    'name': 'Cleo',
    'age': 16,
    'grade': 10
}

student_3 = {
    'name': 'Ada',
    'age': 16,
    'grade': 10
}

def hash_function(key):
    return sum([ord(c) for c in key]) % HASH_TABLE_SIZE


def inset(student):
    hash_table[hash_function(student['name'])].append(student)

def get(student_name):
    for student in hash_table[hash_function(student_name)]:
        if student['name'] == student_name:
            return student

print(hash_table)
inset(student_1)
print(hash_table)
inset(student_2)
print(hash_table)
inset(student_3)
print(hash_table)
print(get('Cleo'))



students = {
    student_1['name']: student_1,
    student_2['name']: student_2,
    student_3['name']: student_3
}

students['Ada']
print(hash('Ada'))
