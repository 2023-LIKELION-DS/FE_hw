mbti = ['INFP', "ENFP", "ISTJ", "ESTJ"]

print(mbti)
print(mbti[0])

mbti[0] = 'INFJ'

print(mbti)
print(mbti[0])

my_list = [123, 'apple']
print(my_list)

colors = ['red', 'blue', 'green']

colors[2] = 'black'
print(colors)

colors.append('purple')
print(colors)

colors.insert(1, 'yellow')
print(colors)

del colors[0]
print(colors)

colors.pop(0)
print(colors)

color = colors.pop(0)
print(colors)
print(color)

colors.remove('black')
print(colors)

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']
colors_2 = colors[:]

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

sorted(colors)
print(colors)

print(sorted(colors))

print(len(colors))

print(colors[1:5])
print(colors[:4])
print(colors[2:])
print(colors[-5:])

print(colors_2)

colors_2.pop()

print(colors)
print(colors_2)

scores = [88, 100, 96, 43, 65, 78]
scores.sort(reverse=True)
print(scores)

for score in scores:
    if score >= 80:
        print(score)
    else:
        print("Fail")

max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores)
avg_val = sum(scores) / len(scores)

tup = (1, 20, 40)
print(tup[0])

tup = (100, 30, 4)
print(tup)

for x in tup:
    print(x)

list_1 = list(tup)
print(list_1)

list_2 = [x for x in tup]
print(list_2)

list_3 = []
for x in tup:
    list_3.append(x)
print(list_3)

student = {
    "syudent_no": "202301234",
    "major": "English",
    "grade": 1
}

print(student["student_no"])

student["student_no"] = "202301235"

print(student)
print(student["student_no"])

student["gpa"] = 4.5
print(student)

student["gpa"] = 4.3
print(student)

del student["grade"]
print(student)

print(student.get("major"))
print(student.get("gpa", "해당 키-값 쌍이 없습니다."))

print(student.keys())
print(list(student.keys()))

print(student.values())
print(list(student.values()))

tech = {
    "HTML": "Advamced",
    "JavaScript": "Intermidiate",
    "Python": "Expert",
    "Go": "Novice"
}

for key, value in tech.items():
    print(f'{key} - {value}')

for key in tech.keys():
    print(key)

for value in tech.values():
    print(value)

student_1 = {
    "student_no": "1",
    "gpa": "4.3"
}

student_2 = {
    "student_no": "2",
    "gpa": "3.8"
}

students = [student_1, student_2]

for student in students:
    print(student)

for student in students:
    print(student['student_no'])

for student in students:
    student['graduated'] = False
    print(student)

student = {
    "subjects": ["회계원리", "중국어회화"]
}

print(student["subjects"])

subjects_list = student["subjects"]

for subject in subjects_list:
    print(subject)

student = {
    "scholarship": {
     "name": "국가장학금",
     "amount": "100000"
    }
}

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    for value_2 in value.values():
        print(value_2)