# 문자열(Strings) = 문자의 나열
city = "seoul" # Seoul, SEOUL, SEOul
print(city)

city.upper() # 대문자로
print(city.upper())

city = city.upper()
print(city)

city.lower() # 소문자로
print(city.lower())

city = city.lower()
print(city)
print()


occupation = "   developer   " # 공백도 문자로 취급
print(occupation)

occupation.rstrip() # 우측 공백을 제거
print(occupation.rstrip())

occupation.lstrip() # 좌측 공백을 제거
print(occupation.lstrip())

occupation.strip() # 모든 공백을 제거
print(occupation.strip())
print()


print("INFP\nENFP\nISTJ\nESTJ") # 줄 바꿈
print("INFP\tENFP\tISTJ\tESTJ") # tap
print()


score = "점수:90"
print(score.removeprefix("점수:")) # 원하지 않는 글자 삭제

score_2 = "75점"
print(score_2.removesuffix("점"))
print()


place = "서울 중구"
print(place.replace("서울", "서울시")) # 글자 변경
print()


si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

# 서울시 종로구
# 용인시 기흥구
# (시의 이름)시 (구의 이름)구
print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구")