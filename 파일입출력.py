from encodings import utf_8


# # 파일 입출력


# # 파일 쓰기

# score_file = open("score.txt", "w", encoding= "utf_8") # score 파일에다가 w(write) 덮어쓴다(기록), 없는 파일이면 알아서 만들어줘!!
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close() # 파일을 열었으니 닫아줘


# score_file = open("score.txt", "a", encoding= "utf_8") # a(append) 덮어쓰지 말고 이어서 써줘
# score_file.write("과학 : 100")
# score_file.write("\n코딩 : 100")

# # 파일 읽기

score_file =  open("score.txt", "r", encoding="utf-8")
print(score_file.read()) # 파일의 글을 전부 읽을거야
score_file.close()

score_file =  open("score.txt", "r", encoding="utf-8")
print(score_file.readline()) # 한줄만 읽기, 한 줄 읽고 커서는 다음 줄로 이동해 즉, 파일에 4줄이 있으면 출력문 4개를 입력해야해
print(score_file.readline(), end="") # 위와 다르게 다음줄이 아닌 이어서 출력이 되
score_file.close()
# 파일읽기1 - 파일에 몇줄이 입력 되어있는지 모를때
score_file =  open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
# 파일 읽기2 - 파일의 모든 줄을 리스트에 저장해
score_file =  open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # line 과 다르게 liens는 리스트 형식으로 저장!
for line in lines:
    print(line, end="")

score_file.close()

# 끄적끄적
'''
이대로 실행하면 오류가 발생할건데 그 이유는 W(읽기)가 주석 처리되어있어서 score.txt 파일이 생성되지 않았기 때문.

score_file.write("과학 : 100") or score_file = open("score.txt", "w", encoding= "utf_8")
--> .write는 다른것과 다르게 자동적으로 줄바꿈(\n)이 안되기에 설정이 필요. 
print(score_file.readline()) 한줄만 읽기에 모든 줄을 읽을려면 반복문이 필요해
'''