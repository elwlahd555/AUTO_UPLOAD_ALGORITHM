
import sys
from collections import deque

num = int(sys.stdin.readline())
num_list=deque()

for i in range(num):
    word = list(sys.stdin.readline().split())
    if word[0]=='push':
        num_list.append(int(word[1]))
    elif word[0]=='front':
        if len(num_list)==0:
            print('-1')
        else:
            print(num_list[0])
    elif word[0]=='back':
        if len(num_list)==0:
            print('-1')
        else:
            print(num_list[len(num_list)-1])
    elif word[0]=='pop':
        if len(num_list)==0:
            print('-1')
        else:
            print(num_list.popleft())
    elif word[0]=='size':
        print(len(num_list))
    elif word[0]=='empty':
        if len(num_list)==0:
            print(1)
        else :
            print(0)