
def solution(array, n):
    answer = 0
    check = 10000
    array.sort()
    for i in array:
        if abs(i-n)<check:
            answer = i
            check = abs(i-n)
        else:
            break
    return answer