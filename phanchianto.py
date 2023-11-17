import math
def nto(n):
    if n < 2:
        return False
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

n = int(input())
a = []
for x in input().split():
    if int(x) not in a:
        a.append(int(x))
ok = False
for i in range(0,len(a)):
    sum1 = sum2 = 0
    for j in range(0,i+1):
        sum1 += a[j]
    for k in range(i+1,len(a)):
        sum2 += a[k]
    if nto(sum1) == True and nto(sum2) == True:
        print(i)
        ok = True
        break
if ok == False:
    print("NOT FOUND")

