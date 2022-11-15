def solution(my_str, n):
    answer = []
    words=''
    k = 0
    for i in my_str:
        words += i
        k += 1
        if k==n:
            answer.append(words)
            words=''
            k=0
    if words != '':
        answer.append(words)
    return answer