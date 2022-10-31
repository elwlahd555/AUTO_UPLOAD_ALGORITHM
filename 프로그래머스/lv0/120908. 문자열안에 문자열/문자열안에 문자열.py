def solution(str1, str2):
    answer = 2
    if str1.find(str2)>=0:
        answer = 1
    return answer