import itertools
a,b = map(int,input().split())
ds = list(map(int,input().split()))
set1 = set()
for x in ds:
    set1.add(x)
rs = list()
for x in set1:
    rs.append(x)
rs.sort()
kq = itertools.combinations(rs,b)
for i in kq:
    for j in range(0,b):
        print(i[j], end=" ")
    print()