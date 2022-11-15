def solution(spell, dic):
    answer = 2
    spell.sort()
    spell = ''.join(spell)
    for word in dic:
        temp = list(word)
        temp.sort()
        temp = ''.join(temp)
        if temp == spell:
            answer = 1
            break
    return answer