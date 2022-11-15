def solution(s):
    answer = ''
    words = list(s)
    words.sort()
    count = 0
    before = words[0]
    for i in range(1,len(words)):
        if before == words[i]:
            count +=1
        elif count == 0:
            answer += before
        else:
            count = 0
        before = words[i]
    if count == 0 :
        answer += words[-1]
    return answer