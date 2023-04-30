if True:
    print("True")
else:
    print("False")

if 4 > 3:
    print("a")
else:
    print("b")

value = input("값을 입력해주세요: ")

if int(value) > 10:
    print("a")
else:
    print("b")

value = value.upper()

if value == "INFP":
    print("INFP")
else:
    print("nothing")

day = input("요일을 입력해주세요(0~6): ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
elif day == "1":
    print("연장영업")
else:
    print("정상영업")

i = 0
sum = 0

for i in range(1, 101):
    print(i)


for i in range(1, 101):
    sum = sum + i
print(sum)

while True:
    print("while loop")

progress = 0

while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed")