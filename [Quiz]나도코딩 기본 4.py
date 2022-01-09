# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
#규칙1 : https// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                (nav)              (5)             (1)
# 예) http://naver.com의 비밀번호는 nav51! 입니다.







#내가 짠 것
ur1 = "https//naver.com"
ur2 = ur1[7:] # naver.com
ur3 = ur2[:-4] # naver

pw1 = ur3[0:3] #nav
pw2 = len(ur3) # c의 문자개수
pw3 = ur3.count("e") # c의 n이 몇개인가.

print(f"생성된 비밀번호 : {pw1}{pw2}{pw3}!")

# 모범답안
'''
url = "https//naver.com"
my_str = url.replace("https//", "") # 규칙1
# https// 부분을 빈칸으로 교체
#print(my_str)
my_str = my_str[:my-str.index(".")] # 규칙2
# my_str[0:5] -> 0~5직전(01234)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url}의 비밀번호는 {passward}입니다.")
'''


# 피드백

"""모범답안과 다르게 변수가 너무 많아 혼란(햇갈림)을 유발할 수 있음.
규칙 1의 .replace를 잘 못 이해한거 같음. 저렇게 응용 할 수 있단걸 깨달음.
규칙 2의 my_str[:my-str.index(".")]를 통해 내가 문자길이를 세지 않아도 찾아서 지정만 해주면 실행됨.
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
처럼 한 변수에 + 해주어도 된다. 간결해지고 효율적으로 변함."""