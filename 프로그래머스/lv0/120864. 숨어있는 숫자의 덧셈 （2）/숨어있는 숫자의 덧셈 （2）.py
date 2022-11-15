def solution(my_string):
    answer = 0
    words = ''
    for i in my_string:
        if i.isdigit():
            words += i
        elif words != '':
            answer += int(words)
            words = ''
    if words != '':
        answer += int(words)
    return answer