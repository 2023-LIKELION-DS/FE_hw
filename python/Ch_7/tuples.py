# 튜플(Tuples)

# tup = (1, 20, 40)
# print(tup[0])

# tup[0] = 100 -> 튜플은 값의 변경이 불가

# tup = (100, 30, 4)
# print(tup)

# for x in tup :
#     print(x)

tup = (1, 20, 40)

# 리스트 변환 1
list_1 = list(tup)
print(list_1)

# 리스트 변환 2
list_2 = [x for x in tup]
print(list_2)

# 리스트 변환 3
list_3 = []

for x in tup :
    list_3.append(x)
print(list_3)