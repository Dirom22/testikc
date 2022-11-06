from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]

max = 0
for i in range(n):
    for j in range(n):
    	if(m[i][j]>max):
            max = m[i][j]
for i in range(n):
    print(m[i])
    print(max)
