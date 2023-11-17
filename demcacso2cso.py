xau = input()
a = []
tmp = ""
for x in range(0,len(xau)-1,2):
    tmp = tmp + xau[x] + xau[x+1]
    if len(tmp) == 2:
        a.append(int(tmp))
        tmp = ""

for x in range(0,len(a)-1):
    dem = 1
    if len(str(a[x])) == 2:
        for y in range(x+1,len(a)):
            if a[y] == a[x]:
                dem += 1
                a[y] = 0
        print(f"{a[x]} {dem}")
