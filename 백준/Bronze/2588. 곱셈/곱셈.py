# input() 을 통해서 한줄씩 받아올 수 있다
A = int(input())
B = input()
#print(A*int(B[2]))
#print(A*int(B[1]))
#print(A*int(B[0]))
#print(A*int(B))
print(A*int(B[2]),A*int(B[1]),A*int(B[0]),A*int(B), sep='\n')