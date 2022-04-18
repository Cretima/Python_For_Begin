

words = ["nice", "happy", "hello", "world", "hi"]
memo = [0,0,0,0,0]
memo1 = [0,0,0,0,0,0,0,0,0]
memo = list(words[0]) # ['n', 'i', 'c', 'e']
print(memo, type(memo), len(memo)) # ['n', 'i', 'c', 'e'] <class 'list'> 4
print(memo[0]) # n




def solution(K, words):
    n = 0 # 몇번째 줄
    nn = 0
    
    memo = [0 for _ in range(K)] # K 줄 메모장 생성
    memo2 = [0 for _ in range(K)] # K 줄 메모장 생성
    True_memo = [0 for _ in range(K)] # K 줄 메모장1 생성

    for i in range(len(words)):
        memo = list(words[i]) # ['n', 'i', 'c', 'e']

        if (i+1) > len(words):# 만약 댜음단어가 존재하지 않으면
            break
        
        for j in range(len(memo)): 
            True_memo[nn] = memo[j] # ['n', 'i', 'c', 'e', '0', '0'] 
            

            memo2 = list(words[i+1])
            
            
        if(len(memo2)) >= True_memo.count(0): # 다음단어가 빈칸보다 초과
            n += 1 # 메모장 한줄 추가
            nn = 0
            True_memo = [0 for _ in range(K)] # 메모 초기화

        else:
            nn += 1 # 아니라면 공백 추가

    answer = n
    return answer




K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(K, words)
print("solution 함수의 반환 값은", ret, "입니다.")
