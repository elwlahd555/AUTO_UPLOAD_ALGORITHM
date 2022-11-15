def solution(my_string):
    answer = 0
    my_string=my_string.split(' ')
    answer += int(my_string[0])
    point = ''
    for i in range(1,len(my_string)):
        if i % 2 == 1:
            point = my_string[i]
        elif point == '+':
            answer += int(my_string[i])
        else:
            answer -= int(my_string[i])
            
    return answer