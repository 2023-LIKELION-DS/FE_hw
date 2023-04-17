# 딕셔너리(Dictionaries)

# student = {
#     "student_no" : "20210862",
#     "major" : "Software",
#     "grade" : 3
# }

# print(student["student_no"])

# student["student_no"] = "202108620"

# print(student)
# print(student["student_no"])

# 추가
# student["gpa"] = 4.5
# print(student)

# # 수정
# student["gpa"] = 4.3
# print(student)

# # 삭제
# del student["grade"]
# print(student)


# student = {
#     "student_no" : "20210862",
#     "major" : "Software",
#     "grade" : 3
# }

# # 데이터 접근
# print(student.get("major"))
# print(student.get("gpa", "해당 키-값 쌍이 없습니다."))

# 딕셔너리의 키를 반환
# print(list(student.keys()))

# 딕셔너리의 값을 반환
# print(list(student.values()))


# tech = {
#     "HTML" : "Advanced",
#     "JavaScript" : "Intermediate",
#     "Python" : "Expert",
#     "Go" : "Novice"
# }

# for i in tech : # 키 값만 반환
#     print(i)

# for key, value in tech : # 접근 불가 오류
#     print(f'{key} - {value}')

# for key, value in tech.items() : # 맞는 방법
#     print(f'{key} - {value}')

# for value in tech.values() : # value만
#     print(value)

# for key in tech.keys() : #key만
#     print(key)


# 중첩(Nesting)

# student_1 = {
#     "student_no" : "1",
#     "gpa" : 4.3
# }

# student_2 = {
#     "student_no" : "2",
#     "gpa" : "3.8"
# }

# students = [student_1, student_2]

# # for student in students :
# #     print(student['student_no'])

# for student in students :
#     student['graduated'] = False
#     print(student)


# student = {
#     "subjects" : ["회계원리", "중국어회화"]
# }

# print(student["subjects"])

# subjects_list = student["subjects"]

# for subject in subjects_list :
#     print(subject)


student = {
    "scholarship" : {
        "name" : "국가장학금",
        "amount" : "1000000"
    }
}

print(student)

for key in student.keys() :
    print(key)

for value in student.values() :
    for value_2 in value :
        print(value_2)