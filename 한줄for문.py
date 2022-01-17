# continue, break 사용

absent = [2, 5] # 결석
no_book = [7] # 책 부재

for student in range(1, 11): # 1~ 10
    if student in absent: # 학생 중 결석이 있다면 넘김.
        continue # 다음 문장으로 실행시키지 않고 다음 반복문 진행
    elif student in no_book: # 학생 중 책이 없다면 
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와.")
        break  # 더이상 진행하지 않고 반복문 탈출
    print(f"{student}, 책을 읽어봐")

# 한줄 for문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 결정 -> 101, 102, 103

students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students] # 리스트 students에 있는 i를 하나씩 가져와 100씩 더해 리스트 저장
print(students) # [101, 102, 103, ...]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor","I am groot"]
students = [len(i) for i in students] # students 값을 idp 주고 길이로 반환 다시 students 대입
print(students) #(8, 4, 10)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor","I am groot"]
students = [i.upper() for i in students] # 모두 대문자 출력.
print(students) 