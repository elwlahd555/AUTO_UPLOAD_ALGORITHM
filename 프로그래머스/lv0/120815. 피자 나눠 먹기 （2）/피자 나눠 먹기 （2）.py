def solution(n):
    answer = 0
    while True:
        answer += 1
        if answer*6%n ==0 :
            break
    
    return answer