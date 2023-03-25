import itertools
xau = input()
kq = list()
for x in range(0,len(xau)):
    kq.append(xau[x])
ds = itertools.permutations(kq,len(xau))
for i in ds:
    for j in range(0,len(xau)):
        print(i[j],end="")
print()