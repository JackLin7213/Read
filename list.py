#It's a list.
students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for student in students:
    print('Hi', student)
x = 0
y = 3
for line in students:
    print(students[x])
    x = x + 1 
    if x == 3:
        break
print ('END')