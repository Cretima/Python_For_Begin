# 집합, 세트 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3} 중복이 안되기에 무시

# 정렬
sorted(my_set)

java = {"유재석", "김태호", "양세형"} 
python = set(["유재석", "박명수"]) # 위에랑 똑같음

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

#합집합 (java 도 할 수 있거나 python도 할 수 있는)
print(java | python) # {'박명수', '김태호', '유재석', '양세형'}
print(java.union(python)) # 순서는 상관 X

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요 ㅠㅠ
java.remove("김태호")
print(java) # {'양세형', '유재석'}
