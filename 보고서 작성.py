
''' 
끄적끄적
문제 : 매주 1회씩 보고서(.txt)를 작성해야해 파일 입출력을 이용해 만들어보자.

반복문, 파일 입출력
매주 1회 - X(1 ~ ?) 주차(반복문) - 파일 쓰기
어떻게 하면 보고서 작성부분을 간략화 할 수 있을까?
--> with로 더 줄여볼까 해. --> 파일에서 사용자 입력이 너무 어려워.
+ 매주 1회가 아닌 매주 n회로 고쳐봐야지. --> report_w 함수를 반복(이중 반복)을 하면 될거 같에.
'''

from encodings import utf_8
import re


def report_write(): # 보고서 작성 함수
    num = 1 # 몇 주차인가?

    while(num < 3): # 지정된 주차까지 보고서 반복 작성

        # # method 1.
        # report_file = open("%d주차.txt" %num, "w", encoding="utf_8")

        # print(f"- {num} 주차 주간 보고 -", file = report_file) # 보고서 <title>

        # # 보고서 작성 부분
        # print("%d 주차 보고서를 쓰는 중이야" %num) # 몇 주차 보고서를 쓰는지 알기 쉽게 할거야
        # department = input("부서명 : ")
        # name = input("자기 이름 : ")
        # contents = input("업무 요약글 : ")

        # print(f"부서 : {department} \n이름 : {name} \n업무 요약 : {contents}", file = report_file) # 적은 내용을 txt파일에 써줘

        # report_file.close() # 보고서 작성 끝 파일을 닫아줘.
        # num += 1 # 주차를 늘려줘


        # # method 2
        with open("%d주차.txt" %num , "w", encoding="utf_8") as report_file :
            print(f"- {num} 주차 주간 보고 -", file = report_file) # 보고서 <title>

            print("%d 주차 보고서를 쓰는 중이야" %num) # 몇 주차 보고서를 쓰는지 알기 쉽게 할거야

            department = input("부서명 : ")
            name = input("자기 이름 : ")
            contents = input("업무 요약글 : ")

            print(f"부서 : {department} \n이름 : {name} \n업무 요약 : {contents}", file = report_file) # 적은 내용을 txt파일에 써줘

            num += 1
            
# # main

# 매주 1회만 작성한다고 가정해
report_write()

# 파일이 잘 저장되었는지 확인용 read
# report_file = open("1주차.txt", "r", encoding="utf_8")
# print(report_file.read()) # 파일안에 있는 글을 전부 읽어줘
# report_file.close()
