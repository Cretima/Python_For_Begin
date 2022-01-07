'''
# 슬라이싱
krID = "990401-1234567"

print("성별 : ", krID[7]) # 0~14 중 7번째 가져오기
print("연(year) : ", krID[0:2]) # 0부터 2 직전까지(0, 1)가져오기
print("월(Month) : ", krID[2:4])
print("일(Day) : ", krID[4:6])

print("생년월일 : ", krID[:6]) # 처음부터 6직전까지
print("뒤 7자리 : ", krID[7:]) # 7번째부터 끝까지
print("뒤 7자리(뒤에부터) : ", krID[-7:]) 
# 맨 뒤(-1)에서 7번째부터 끝까지
'''
#
python = "Python is Amazing"
print(python.lower()) #모두 소문자로 표기,python is amazing
print(python.upper()) #대문자 표기
print(python[0].isupper) #이 문자열의 0번째가 대문자인가? 맞으면 True 출력

