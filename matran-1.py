n = int(input())
a = [[]]*n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
s1 = s2 = 0
for i in range(n):
    for j in range(n):
        if i < j:
            s1 += a[i][j]
        elif i > j:
            s2 += a[i][j]
kq = abs(s1-s2)
if kq <= k:
    print("YES")
else:
    print("NO")
print(kq)
