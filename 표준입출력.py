# print("Python", "Java", "JavaScript", sep=",", end="?") # seperate
# # Python,Java,JavaScript?  

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.iteams(): # iteams key와 value를 subject와 score로 보냄
#     print(subject, score)
#     print(subject.ljust(6), str(score).rjust(4), sep=":") #ljust(i) 왼쪽(left)으로 정렬하데 총 i만큼 확보해라. 

# # 은행 대기순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(i) i칸을 확보하는데 빈공간을 0으로 채워라
#     # 대기번호 : 001    대기번호 : 002..

# answer = input("아무 값이나 입력하세요. : ") # 입력한 값을 문자열로 저장됨
# print(f"입력하신 값은 {answer} 입니다.") 