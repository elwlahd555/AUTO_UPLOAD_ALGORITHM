import sys
from collections import deque

num = int(sys.stdin.readline())

num_list=deque(range(1,num+1))

while len(num_list)>1:
    num_list.popleft()
    num_list.append(num_list.popleft())

print(num_list[0])