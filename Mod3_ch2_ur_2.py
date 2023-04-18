from random import randint
n = 5
m = [[ randint (0,100) for i in range (n)] for j in range (n)]
#list = [max (m)]
#print (max (list))
m.sort()
print (m[0])
