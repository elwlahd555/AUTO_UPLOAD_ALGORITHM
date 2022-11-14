def solution(before, after):
    answer = 1
    before=list(before)
    before.sort()
    after=list(after)
    after.sort()
    for i in range(len(before)):
        if before[i] != after[i]:
            answer = 0
            break
    return answer