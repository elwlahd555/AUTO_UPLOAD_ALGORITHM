def solution(n):
    answer = 0
    num = 1
    for i in range(1, 11):
        num *= i
        if num == n:
            answer = i
            break
        elif num > n:
            answer = i-1
            break
    return answer