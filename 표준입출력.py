# 영상에선 print("{0}".format(a)) 형식으로 입력하지만 나의 편의를 위해 바꾸면서 공부중.

# print("Python", "Java", "JavaScript", sep=",", end="?") # seperate
# # Python,Java,JavaScript?  

# import sys # sys 모튤 - 변수와 함수를 직접 제어할수있는 모듈
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.iteams(): # iteams key와 value를 subject와 score로 보냄
#     print(subject, score)
#     print(subject.ljust(6), str(score).rjust(4), sep=":") #ljust(i) 왼쪽(left)으로 정렬하데 총 i만큼 확보해라. 

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(i) i칸을 확보하는데 빈공간을 0으로 채워라 # zfill == zerofill이 아닐까 생각.
#     # 대기번호 : 001    대기번호 : 002..

# answer = input("아무 값이나 입력하세요. : ") # 입력한 값을 문자열로 저장됨
# print(f"입력하신 값은 {answer} 입니다.")


# # 출력 포멧(format)
# 빈자리는 빈공간으로 두고, 오른쪽 정렬 하되, 총 10자리 공간을 확보
print(f"{500: >10}") # :과 >(오른쪽 정렬) 사이의 공백(빈공간) >> 만약 빈공간 대신 1을 넣으면 1111111500
# == print(f"{500:>10}") 위에 빈칸을 띄우는 이유는 가독성을 위해 또는 무엇이 들어가야하는지 알려주기 위해 띄운것 같다.

# 양수일 땐 +로 음수일 땐 -로 표시
print(f"{500: >+10}") # +500    바로 위 출력문과 다르게 +가 붙음.
print(f"{-500: >+10}") # -500

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print(f"{500:_<10}") # 500______

# 가운데 정렬
print(f"{500: ^10}")

# 3자리 마다 콤마를 찍어주기
print(f"{1000000000:,}") # 1,000,000,000
# 3자리마다 콤마를 찍어주기, +=부호 붙이기
print(f"{1000000000:+,}") # +1,000,000,000
print(f"{-1000000000:+,}") # -1,000,000,000
# 3자리 마다 콤마를 찍어주기, 부호도붙이고, 자릿수 확보
# 돈이 많으면 행복하니깐 빈 자리는 ^ 로 채워주기
print(f"{1000000000:^<+20,}") # +1,000,000,000^^^^^^
# 소수점 출력
print(f"{5/3:f}")
# 소수점 특정 자리수까지 표사 (소수점 3째 자리에서 반올림)
print(f"{5/3:.2f}") # 만약 0.2f를 찍으면 남는 자리수가 0으로 출력.


# 정리 : sys는 매커니즘을 모르겠어서 다시 공부 필요, .rjust(i) 와 0: >10 의 차이는 문자열(str)과 정수(int)의 차이.
