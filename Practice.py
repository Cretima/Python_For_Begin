'''
# 슬라이싱 // 나도코딩 4-2
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
# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) #모두 소문자로 표기 // python is amazing
print(python.upper()) #대문자 표기
print(python[0].isupper) #이 문자열의 0번째가 대문자인가? 맞으면 True 출력
print(len(python)) #해당 문자열의 길이를 구해줌 17
print(python.replace("Python", "java")) # Java is Amazing
#해당 문자열의 문자를 찾은 후 그 부분 바꿔서 출력

index = python.index("n") # n이 몇번째에 위치하는가?
print(index) # 5번째 위치
index = python.index("n", index + 1) # 찾은위치(5번째) 그 다음부터 찾기 즉, 두번째 n찾기
print(index) # 15

print(python.find("n")) # 위(.index)와 비슷함 but 차이는
print(python.find("Java")) # -1 출력 밑에 프로그램 계속.
# print(python.index("Java")) # 에러 발생. 그리고 프로그램 끝냄.

print(python.count("n")) # 해당 변수(Python)에 n이 몇개냐? // 2
