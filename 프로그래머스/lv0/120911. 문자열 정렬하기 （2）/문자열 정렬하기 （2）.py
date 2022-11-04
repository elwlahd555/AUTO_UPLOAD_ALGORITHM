def solution(my_string):
    answer = ''
    str_list=[]
    for i in my_string:
        str_list.append(i.lower())
    str_list.sort()
    for i in str_list:
        answer += i
    return answer