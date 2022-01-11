##리스트 [] 순서를 가지는 객체의 집합

# EX) 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30] # 위에걸 한번에 묶어줌
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 활용 : 조세호씨가 몇 번째 칸에?
print(subway.index("조세호")) # 1

# 하하씨가 다음 정류장에서 탐 .append : 추가
subway.append("하하")
print(subway)

# 정현돈씨를 유재석 / 조세호 사이에 태움 .insert
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄 .pop
print(subway.pop()) # 하하
print(subway) # ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명있는지
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 2

# 정렬도 가능 .sort
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1,2,3,4,5]

# 순서 뒤집기 가능 .reverse
num_list.reverse()
print(num_list)

# 모두 지우기 .clear
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장(합치기) .extend
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]


## 튜플 / 리스트와 다르게 추가 제거 불가 but 처리속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

#menu.add("생선까스") # add 기능지원 X 오류발생

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
