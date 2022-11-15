def solution(emergency):
    answer = []
    numbers = emergency.copy()
    numbers.sort(reverse = True)
    for i in emergency:
        answer.append(numbers.index(i)+1)
    return answer