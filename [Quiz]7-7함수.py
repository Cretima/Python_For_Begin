# Quiz) 표준 체중을 구하는 프로그램 작성

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시


# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.






def std_weight(height, gender):
    weight = 0
    if gender == "남자":
        weight = (height * 0.01) * (height * 0.01) * 22
        print(f"키 {height}cm 남자의 표준 체중은 {weight:0.2f}kg 입니다.")
    else:
        weight = (height * 0.01) * (height * 0.01) * 21
        print(f"키 {height}cm 여자의 표준 체중은 {weight:0.2f}kg 입니다.")
         
height = 173
gender = "여자"

std_weight(height, gender) # or std_weight(height / 100, gender) 하고 위의 *0.01 제거


# 최적화 및 모범답안

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
         
height = 173
gender = "여자"
weight = std_weight(height * 0.01, gender)
print(f"키 {height}cm {gender}의 표준 체중은 {weight:0.2f}kg 입니다.")

# 피드백
'''
문제를 해결하는 것도 중요하지만 끝내고 안주하지 않고 최적화, 클린코드를 위해 항상 고민하는 자세가 필요
'''
