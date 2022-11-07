def solution(my_string, num1, num2):
    answer = ''
    temp=list(my_string)
    temp[num1]=my_string[num2]
    temp[num2]=my_string[num1]
    answer = ''.join(temp)
    return answer