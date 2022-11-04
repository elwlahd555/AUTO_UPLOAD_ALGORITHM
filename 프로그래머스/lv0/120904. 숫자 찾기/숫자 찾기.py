def solution(num, k):
    answer = -1
    if str(num).find(str(k)) >=0:
        answer=str(num).find(str(k))+1

    return answer