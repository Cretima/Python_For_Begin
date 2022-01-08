
# 깔끔한 출력을 위한 자릿수 또는 소수점 결정.
print("%d" %123) #123
print("%5d" %123) #  123
print("%05d\n" %123) #00123

print("%f" %123.46) #123.460000
print("%7.1f" %123.46)#  123.5
print("%7.3f\n" %123.46)#123.460

print("%s" %"Python")#Python
print("%10s" %"Python")#     Python

# 이스케이프 함수
print("\n줄바꿈\n연습")
print("\t탭키\t연습")
 # \n : "
print("글자가\"강조\"되는 효과1")
# \' : '
print("글자가\'강조\'되는 효과2") 
 # // : /
print("\\\\\\ 역슬레시 세 개 출력")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple로 출력.
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple 출력.
print(r"\n \t \" \\를 그대로 출력")

#숫자 처리함수
print(abs(-5)) # 절댓값 5
print(pow(4, 2)) # 4^2 = 4 **2 = 16
print(max(5, 12)) # 최댓값 12
print(min(5, 12)) # 최솟값 5
print(round(3.14)) # 반올림 3
print(round(4.99)) # 5

from math import *
print((floor(4.99))) # 내림. 4
print((ceil(4.99))) # 올림. 5
print(sqrt(16)) # 제곱근. 4'''

#랜덤함수
from random import * # 랜덤함수 수입.

print(random()) # 0.0 ~ 1.0 미만 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값