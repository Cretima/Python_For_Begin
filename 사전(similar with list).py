# 사전 {} # 키와 벨류로 이루어져 있음 즉  키1 <-- 벨류1 , 키2 <-- 벨류2
# EX) 여러개의 사물함 중 한사람당 번호에 해당하는 사물함 키를 가지고 있다. 오세현 3번키, 아무개 21번키

#cabinet = {3:"유재석", 100:"조세호"}
# # 방법 1
# print(cabinet[3]) # 유재석
# print(cabinet[100]) # 조세호
# # 방법 2
# print(cabinet.get(3)) # 유재석
# # 방법 1,2의 차이점
# #print(cabinet[5]) # 지정된 5키가 없으므로 KeyEroor 5 오류출력 후 프로그램 end
# print(cabinet.get(5)) # None 출력하고 다음 코드실행
# print(cabinet.get(5, "사용가능")) # 사용가능 출력
# print("hi")

# # 변수에 해당 값이 들어있는가? in
# print(3 in cabinet) # True
# print(5 in cabinet) # False


# 정수 아닌 문자일때
cabinet = {"A-3":"유재석", "B-100":"조세호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 조세호

# 새 고객
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
# if C-20이 이미 사용중이면 업데이트가 되서 조세호로 변경
print(cabinet)

# 고객 떠남
del cabinet["A-3"]
print(cabinet) # [A-3] 사용자 삭제

# Key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘다 출력
print(cabinet.items())

# 폐점
# cabinet.clear
print(cabinet.clear) # {}
