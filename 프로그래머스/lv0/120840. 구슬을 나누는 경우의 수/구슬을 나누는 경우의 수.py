def solution(balls, share):
    answer = 1
    for i in range(balls-share+1,balls+1):
        answer = answer * i / (i-balls+share)
    return answer